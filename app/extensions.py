from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = "auth.login"

bcrypt = Bcrypt()
db = SQLAlchemy()
