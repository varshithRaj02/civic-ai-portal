import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploads")
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB


class Config:
    SECRET_KEY = "super-secret-key"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_url = os.getenv("DATABASE_URL") or "sqlite:///civic.db"

    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "app/static/uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    DEBUG = False
