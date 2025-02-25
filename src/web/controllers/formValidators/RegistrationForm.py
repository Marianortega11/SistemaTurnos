from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from src.model.Usuario import Usuario

class RegisterForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")



class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length( min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")