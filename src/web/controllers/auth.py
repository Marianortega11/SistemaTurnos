from datetime import datetime
from sqlite3 import IntegrityError
from flask import Blueprint, flash, redirect, request, session,url_for
from flask import render_template
from src.web.controllers.formValidators.RegistrationForm import RegisterForm, LoginForm
from src.model.Usuario import Usuario


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/login", methods=["GET", "POST"])
def login ():
    form = LoginForm()
    if form.validate_on_submit():
        if Usuario.check_password(form.email.data, form.password.data):
            session["email"] = form.email.data
            return redirect(url_for("home"))
    return render_template("auth/login.html", form = form)


@bp.route("/register", methods=["GET", "POST"])
def register ():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        try:
            Usuario.create(form.email.data, form.password.data)
            return redirect(url_for("auth.login"))
        except ValueError as e:
            flash(str(e), "error")
            return redirect(url_for("auth.register"))

    return render_template("auth/register.html", form = form)