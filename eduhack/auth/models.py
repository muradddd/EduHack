# import pymysql.cursors
from eduhack import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin
from sqlalchemy.sql import func
from eduhack.auth.utils import UserTypeEnum


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    # information
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True ,nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    # user_type = db.Column(db.Enum(UserTypeEnum), default=UserTypeEnum.student, nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    is_superuser = db.Column(db.Boolean(), default=False, nullable=False)
    date_joined = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # relations
    groups = db.relationship('Group', backref='user', lazy=True)

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = generate_password_hash(password)
        # self.user_type = user_type

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


db.create_all()