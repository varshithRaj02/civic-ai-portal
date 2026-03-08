from app.app import create_app
from app.extensions import db, bcrypt
from app.models.models import User

app = create_app()

with app.app_context():

    db.create_all()

    admin_pass = bcrypt.generate_password_hash("admin123").decode("utf-8")
    user_pass = bcrypt.generate_password_hash("user123").decode("utf-8")

    # create admin if not exists
    if not User.query.filter_by(username="admin").first():

        admin = User(
            username="admin",
            email="admin@test.com",
            password=admin_pass,
            role="admin"
        )

        user = User(
            username="user",
            email="user@test.com",
            password=user_pass,
            role="user"
        )

        db.session.add_all([admin, user])
        db.session.commit()

        print("✅ Admin & User created successfully")

    else:
        print("⚠️ Users already exist")