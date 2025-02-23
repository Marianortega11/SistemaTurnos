from datetime import datetime
from flask import Blueprint, flash, redirect, session,url_for
from flask import render_template

bp = Blueprint('turno', __name__, url_prefix='/turnos')

@bp.route("/")
def index():
    return render_template("turnos/index.html")

    """
    Este es el create pero le puse reservar
    """
@bp.route("/reservar")
def reservar():
    return render_template("turnos/reservar.html")

