from app.app import create_app
from app.extensions import db, bcrypt
from app.models.models import User

app = create_app()

with app.app_context():
    db.create_all()

    # delete old admin (important)
    existing = User.query.filter_by(email="admin@test.com").first()
    if existing:
        db.session.delete(existing)
        db.session.commit()

    # create new admin
    admin_pass = bcrypt.check_password_hash("admin123").decode("utf-8")

    admin = User(
        username="admin",   # ✅ ADD THIS
        email="admin@test.com",
        password=admin_pass,
        role="admin"
    )

    db.session.add(admin)
    db.session.commit()

    print("✅ Admin created successfully")