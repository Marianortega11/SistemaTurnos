from datetime import datetime
from flask import Blueprint, flash, redirect, session,url_for
from flask import render_template
from src.model.RegistrationForm import RegisterForm, LoginForm
from src.model.Usuario import Usuario


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/login", methods=["GET", "POST"])
def login ():
    form = LoginForm()
    if form.validate_on_submit():
        if Usuario.check_password(form.username.data, form.password.data):
            session["username"] = form.username.data
            return redirect(url_for("home"))
    return render_template("auth/login.html", form = form)

@bp.route("/register", methods=["GET", "POST"])
def register ():
    form = RegisterForm()
    
    if form.validate_on_submit():
        Usuario.create(form.username.data, form.password.data)
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form = form)