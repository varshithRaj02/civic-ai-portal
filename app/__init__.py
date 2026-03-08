from flask import Flask
from app.extensions import db, bcrypt, login_manager
from flask_migrate import Migrate


def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.user.routes import user_bp
    from app.admin.routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    # Create admin user safely
    with app.app_context():from app.models.models import User

    try:

        if db.engine.dialect.has_table(db.engine.connect(), "users"):

            if not User.query.filter_by(username="admin").first():

                admin = User(
                    username="admin",
                    email="admin@city.gov",
                    password=bcrypt.generate_password_hash("admin123").decode("utf-8"),
                    role="admin"
                )

                db.session.add(admin)
                db.session.commit()

    except Exception:
        pass
    with app.app_context():from app.models.models import User

    try:
        admin = User.query.filter_by(email="admin@city.gov").first()

        if not admin:

            admin = User(
                username="admin",
                email="admin@city.gov",
                password=bcrypt.generate_password_hash("admin123").decode("utf-8"),
                role="admin"
            )

            db.session.add(admin)
            db.session.commit()

            print("✅ Admin account created")

    except Exception:
        pass
    return app