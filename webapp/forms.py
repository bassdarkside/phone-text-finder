from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

from .utils.validators import Unique
from .models import User


class EmailUsernamePasswordForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            DataRequired(),
            Email(),
            Unique(
                User,
                User.email,
                message="There is already an account with that email.",
            ),
        ],
    )
    username = StringField(
        "username",
        validators=[
            DataRequired(),
            Length(min=3, message="Username should be at least 3 characters."),
            Unique(
                User,
                User.username,
                message="There is already an account with that username.",
            ),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=7, message="Password should be at least 7 characters."),
        ],
    )
    password2 = PasswordField("password2", validators=[DataRequired()])


class EmailPasswordForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class PhoneCodeForm(FlaskForm):
    input_number = StringField("input_number", validators=[DataRequired()])
    code = StringField("code", validators=[DataRequired()])
