import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploads")
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB


class Config:
    SECRET_KEY = "super-secret-key"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "civic.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "app/static/uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    DEBUG = False
