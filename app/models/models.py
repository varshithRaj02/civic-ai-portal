from app.extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="user")
    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Complaint(db.Model):
   

    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))
    location = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.Text)
    media = db.Column(db.String(255))
    priority = db.Column(db.String(20), default="Medium")
    status = db.Column(db.String(30), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
