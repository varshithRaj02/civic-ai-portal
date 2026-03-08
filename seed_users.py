from app.app import create_app
from app.extensions import db, bcrypt
from app.models.models import User

app = create_app()

with app.app_context():
    db.create_all()

    # 🔐 passwords
    admin_pass = bcrypt.generate_password_hash("admin123").decode("utf-8")
    user_pass = bcrypt.generate_password_hash("user123").decode("utf-8")

    # 👤 admin
    admin = User(
        email="admin@test.com",
        password_hash=admin_pass,
        role="admin"
    )

    # 👤 user
    user = User(
        email="user@test.com",
        password_hash=user_pass,
        role="user"
    )

    db.session.add_all([admin, user])
    db.session.commit()

    print("✅ Admin & User created successfully")
