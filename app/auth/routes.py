from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.extensions import bcrypt, db, login_manager
from app.models.models import User
from app.utils.tokens import generate_reset_token, verify_reset_token
from flask import current_app

# 🔥 THIS LINE MUST EXIST
auth_bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    if not user_id.isdigit():
        return None
    return db.session.get(User, int(user_id))


@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user, remember=True)

            if user.role == "admin":
                return redirect(url_for("admin.dashboard"))
            else:
                return redirect(url_for("user.dashboard"))

        flash("Invalid email or password")

    return render_template("auth/login.html")
@auth_bp.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing = User.query.filter_by(email=email).first()

        if existing:
            flash("Email already registered")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password,
            role="user"
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth_bp.route("/forgot-password", methods=["GET","POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form.get("email")

        user = User.query.filter_by(email=email).first()

        if user:

            token = generate_reset_token(email)

            reset_link = url_for(
                "auth.reset_password",
                token=token,
                _external=True
            )

            print("PASSWORD RESET LINK:", reset_link)

        flash("If the email exists, a reset link has been sent.")

    return render_template("auth/forgot_password.html")


@auth_bp.route("/reset-password/<token>", methods=["GET","POST"])
def reset_password(token):

    email = verify_reset_token(token)

    if not email:
        flash("Reset link expired")
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(email=email).first()

    if request.method == "POST":

        password = request.form.get("password")

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        user.password = hashed

        db.session.commit()

        flash("Password updated successfully")

        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect("/login")
