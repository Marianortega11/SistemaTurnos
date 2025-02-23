from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from src.model.Usuario import Usuario

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")


def validate_username(self, username):
    usuario = Usuario.query.filter_by(username=username.data).first()
    if usuario:
        raise ValidationError("Username already taken")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")