from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.models import Complaint
import folium
from folium.plugins import HeatMap

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# 🔐 Role Guard
def admin_only():
    return current_user.is_authenticated and current_user.role == "admin"


@admin_bp.route("/dashboard")
@login_required
def dashboard():

    if not admin_only():
        return redirect(url_for("auth.login"))

    # ===============================
    # BASIC STATS
    # ===============================
    total = Complaint.query.count()
    high_priority = Complaint.query.filter_by(priority="High").count()
    pending = Complaint.query.filter_by(status="Pending").count()
    in_progress = Complaint.query.filter_by(status="In Progress").count()
    resolved = Complaint.query.filter_by(status="Resolved").count()

    stats = {
        "total": total,
        "high_priority": high_priority,
        "pending": pending,
        "in_progress": in_progress,
        "resolved": resolved
    }

    # ===============================
    # HIGH PRIORITY TABLE
    # ===============================
    high_priority_complaints = Complaint.query.filter_by(
        priority="High"
    ).order_by(Complaint.created_at.desc()).limit(5).all()

    # ===============================
    # PRIORITY CHART DATA
    # ===============================
    high = Complaint.query.filter_by(priority="High").count()
    medium = Complaint.query.filter_by(priority="Medium").count()
    low = Complaint.query.filter_by(priority="Low").count()

    priority_data = [high, medium, low]

    # ===============================
    # MONTHLY TREND DATA
    # ===============================
    from sqlalchemy import extract

    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]

    month_counts = []

    for i in range(1, 13):
        count = Complaint.query.filter(
            extract("month", Complaint.created_at) == i
        ).count()
        month_counts.append(count)

    # ===============================
    # MAP
    # ===============================
    complaints = Complaint.query.all()

    m = folium.Map(location=[17.3850, 78.4867], zoom_start=12)

    heat_data = []

    for c in complaints:
        if c.latitude and c.longitude:
            heat_data.append([c.latitude, c.longitude])

            folium.Marker(
                [c.latitude, c.longitude],
                popup=f"{c.title} ({c.priority})"
            ).add_to(m)

    HeatMap(heat_data).add_to(m)

    map_html = m._repr_html_()

    # ===============================
    # HOTSPOT DETECTION
    # ===============================
    from collections import Counter
    locations = [c.location for c in complaints if c.location]
    if locations:
        location_counter = Counter(locations)
        top_location = location_counter.most_common(1)[0][0]
    else:
        top_location = "No data"
    
    categories = [c.category for c in complaints if c.category]
    if categories:
        category_counter = Counter(categories)
        top_category = category_counter.most_common(1)[0][0]
    else:
        top_category = "No data"
    
    from collections import Counter
    # ===============================
    # CATEGORY ANALYTICS
    # ===============================
    categories = [c.category for c in complaints if c.category]
    category_counts = Counter(categories)
    category_labels = list(category_counts.keys())
    category_values = list(category_counts.values())

    # ===============================
    # URGENT COMPLAINTS
    # ===============================
    urgent_complaints = Complaint.query.filter_by(priority="High", status="Pending").order_by(Complaint.created_at.desc()).limit(3).all()
    # Detect most problematic location
    locations = [c.location for c in complaints if c.location]
    if locations:
        location_counts = Counter(locations)
        top_location, top_count = location_counts.most_common(1)[0]
    else:
        top_location = "No data"
        top_count = 0

    # Detect most common category
    categories = [c.category for c in complaints if c.category]
    if categories:
        category_counts = Counter(categories)
        top_category, category_count = category_counts.most_common(1)[0]
    else:
        top_category = "No data"
    category_counts = [
    Complaint.query.filter_by(category="Roads").count(),
    Complaint.query.filter_by(category="Water").count(),
    Complaint.query.filter_by(category="Electricity").count(),
    Complaint.query.filter_by(category="Sanitation").count(),
    Complaint.query.filter_by(category="Public Safety").count()
]
    # Emergency complaints detection
    emergency_complaints = Complaint.query.filter(
    Complaint.priority == "High",
    Complaint.status != "Resolved"
).order_by(Complaint.created_at.desc()).limit(5).all()
    # Risk zone detection
    risk_zones = {}
    for c in complaints:
        if c.location:
            risk_zones[c.location] = risk_zones.get(c.location, 0) + 1
    high_risk_zone = None
    high_risk_count = 0
    for loc, count in risk_zones.items():
        if count > high_risk_count:
            high_risk_zone = loc
            high_risk_count = count
    # ===============================
    # RETURN TEMPLATE
    # ===============================
    return render_template(
    "admin/dashboard.html",
    stats=stats,
    high_priority_complaints=high_priority_complaints,
    map_html=map_html,
    priority_data=priority_data,
    months=months,
    month_counts=month_counts,
    category_labels=category_labels,
    category_values=category_values,
    urgent_complaints=urgent_complaints,
    top_location=top_location,
    top_category=top_category,
    category_counts=category_counts,
    emergency_complaints=emergency_complaints,
    high_risk_zone=high_risk_zone,
    high_risk_count=high_risk_count
)

@admin_bp.route("/complaints")
@login_required
def all_complaints():

    if not admin_only():
        return redirect(url_for("auth.login"))

    complaints = Complaint.query.order_by(
        Complaint.created_at.desc()
    ).all()

    return render_template(
        "admin/complaints.html",
        complaints=complaints
    )

@admin_bp.route("/complaint/<int:complaint_id>/status", methods=["POST"])
@login_required
def update_status(complaint_id):

    if not admin_only():
        return redirect(url_for("auth.login"))

    new_status = request.form.get("status")

    complaint = Complaint.query.get_or_404(complaint_id)
    complaint.status = new_status

    db.session.commit()

    return redirect(url_for("admin.all_complaints"))

@admin_bp.route("/complaint/<int:complaint_id>")
@login_required
def complaint_detail(complaint_id):

    if not admin_only():
        return redirect(url_for("auth.login"))

    complaint = Complaint.query.get_or_404(complaint_id)

    return render_template(
        "admin/complaint_detail.html",
        complaint=complaint
    )