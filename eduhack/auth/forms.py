from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Length, Email
from eduhack.auth.models import User
from eduhack import db


class LogInForm(FlaskForm):
    email = StringField('E-poçt', validators=[Length(5, 40), DataRequired()])
    password = PasswordField('Şifrə', validators=[Length(min=8, max=40)])


class RegisterForm(FlaskForm):
    email = EmailField('E-poçt', validators=[Email(), Length(max=40), DataRequired()])
    first_name = StringField('Ad', validators=[Length(max=40), DataRequired()])
    last_name = StringField('Soyad', validators=[Length(max=40), DataRequired()])
    password = PasswordField('Şifrə', validators=[Length(min=8, max=40), DataRequired()])

    def validate_email(self, field):
        exists = db.session.query(db.exists().where(User.email == field.data)).scalar()
        if exists:
            raise ValidationError('E-mail artıq mövcuddur')
        return field

    def validate_password(self, field):
        data = field.data
        cap_letter = [letter for letter in data if 65 <= ord(letter) <= 90]
        if data.isdigit():
            raise ValidationError('Ən azı 1 hərf yazın')
        elif not cap_letter:
            raise ValidationError('Ən azı 1 böyük hərf olmalıdır')
        return field

