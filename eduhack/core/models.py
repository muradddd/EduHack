# import pymysql.cursors
from eduhack import db
from eduhack.auth.models import User
from sqlalchemy.sql import func
from eduhack.auth.utils import UserTypeEnum


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

student_identifier = db.Table('student_identifier',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Group(db.Model):
    # information
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True ,nullable=False)
    language = db.Column(db.String(40), nullable=False)

    # relations
    headmen = db.Column(db.Integer, db.ForeignKey('user.id'))
    students = db.relationship("User",  secondary=student_identifier)

    # moderator
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"{self.name}"


db.create_all()