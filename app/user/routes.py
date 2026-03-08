from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from sqlalchemy import func
import os

from app.extensions import db
from app.models.models import Complaint

# AI modules
from app.ml.predict_priority import predict_priority, model, vectorizer
from app.ml.similarity import find_similar
from app.ml.image_detection import detect_image_risk

user_bp = Blueprint("user", __name__, url_prefix="/user")


# =============================
# USER DASHBOARD
# =============================
@user_bp.route("/dashboard")
@login_required
def dashboard():

    user_id = current_user.id

    total = Complaint.query.filter_by(user_id=user_id).count()
    pending = Complaint.query.filter_by(user_id=user_id, status="Pending").count()
    in_progress = Complaint.query.filter_by(user_id=user_id, status="In Progress").count()
    resolved = Complaint.query.filter_by(user_id=user_id, status="Resolved").count()

    high = Complaint.query.filter_by(user_id=user_id, priority="High").count()
    medium = Complaint.query.filter_by(user_id=user_id, priority="Medium").count()
    low = Complaint.query.filter_by(user_id=user_id, priority="Low").count()

    category_data = db.session.query(
        Complaint.category,
        func.count(Complaint.id)
    ).filter_by(user_id=user_id).group_by(Complaint.category).all()

    categories = [c[0] for c in category_data]
    category_counts = [c[1] for c in category_data]

    monthly_data = db.session.query(
        func.strftime("%m", Complaint.created_at),
        func.count(Complaint.id)
    ).filter_by(user_id=user_id).group_by(
        func.strftime("%m", Complaint.created_at)
    ).all()

    months = [m[0] for m in monthly_data]
    month_counts = [m[1] for m in monthly_data]

    stats = {
        "total": total,
        "pending": pending,
        "in_progress": in_progress,
        "resolved": resolved,
        "high_priority": high
    }

    recent_complaints = Complaint.query.filter_by(
        user_id=user_id
    ).order_by(Complaint.created_at.desc()).limit(5).all()

    return render_template(
        "user/dashboard.html",
        stats=stats,
        recent_complaints=recent_complaints,
        categories=categories,
        category_counts=category_counts,
        months=months,
        month_counts=month_counts,
        high=high,
        medium=medium,
        low=low
    )


# =============================
# SUBMIT COMPLAINT
# =============================
@user_bp.route("/complaint/new", methods=["GET", "POST"])
@login_required
def submit_complaint():

    if request.method == "POST":

        title = request.form.get("title")
        category = request.form.get("category")
        location = request.form.get("location")
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        description = request.form.get("description")

        # AI priority prediction
        priority = predict_priority(description)

        # Similar complaint detection
        past = [c.description for c in Complaint.query.all()]
        similarity_score = find_similar(description, past)
        print("Similarity Score:", similarity_score)

        # Image detection
        image_risk = "None"

        file = request.files.get("media")
        filename = None

        if file and file.filename:

            filename = secure_filename(file.filename)

            upload_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"], filename
            )

            file.save(upload_path)

            # detect risk from image
            image_risk = detect_image_risk(upload_path)

            print("Image Risk:", image_risk)

        # Save complaint
        complaint = Complaint(
            user_id=current_user.id,
            title=title,
            category=category,
            location=location,
            latitude=latitude,
            longitude=longitude,
            description=description,
            media=f"uploads/{filename}" if filename else None,
            priority=priority,
            status="Pending"
        )

        db.session.add(complaint)
        db.session.commit()

        flash("Complaint submitted successfully!", "success")

        return redirect(url_for("user.dashboard"))

    return render_template("user/submit_complaint.html")


# =============================
# USER COMPLAINT LIST
# =============================
@user_bp.route("/complaints")
@login_required
def my_complaints():

    complaints = Complaint.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Complaint.created_at.desc()
    ).all()

    return render_template(
        "user/complaints.html",
        complaints=complaints
    )


# =============================
# AI PRIORITY API
# =============================
@user_bp.route("/ai/predict-priority", methods=["POST"])
def predict_priority_api():

    data = request.get_json()

    description = data.get("description")

    # ML prediction
    X = vectorizer.transform([description])

    prediction = model.predict(X)[0]

    priority = prediction

    severity_score = round(
        float(max(model.predict_proba(X)[0])), 2
    )

    # Risk classification
    if priority == "High":
        risk_type = "Critical Safety"

    elif priority == "Medium":
        risk_type = "Moderate Risk"

    else:
        risk_type = "General Issue"

    return jsonify({
        "priority": priority,
        "severity_score": severity_score,
        "risk_type": risk_type
    })