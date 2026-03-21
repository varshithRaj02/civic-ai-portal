from flask import Flask
from app.config import Config
from app.extensions import login_manager, bcrypt, db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABSE_URL","sqlite:///civic.db"
        )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Upload settings
    app.config["UPLOAD_FOLDER"] = Config.UPLOAD_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = Config.MAX_CONTENT_LENGTH

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.user.routes import user_bp
    from app.admin.routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    print(app.url_map)

    # Health check
    @app.route("/ping")
    def ping():
        return "FLASK IS RUNNING"

    return app