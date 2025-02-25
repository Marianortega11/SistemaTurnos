from datetime import datetime
from flask import Blueprint, flash, redirect, request, session,url_for
from flask import render_template

from src.model.Cancha import Cancha
from src.model.Turno import Horario, Turno
from src.web.controllers.formValidators.turnoForm import FechaForm

bp = Blueprint('turno', __name__, url_prefix='/turnos')

@bp.route("/", methods=["GET", "POST"])
def index():
    form = FechaForm()
    if request.method == 'POST' and form.validate_on_submit():
        fecha = form.fecha.data
        return redirect(url_for("turno.reservar", fecha=fecha))
    return render_template("turnos/index.html", form = form)


"""
    Este es el create pero le puse reservar
"""
@bp.route("/reservar/<fecha>", methods=["GET", "POST"])
def reservar(fecha):
  
    canchas_con_turnos = canchas_con_turnos_disponibles(fecha)
    
    if request.method == 'POST':
        horario = request.form.get("horario")
        cancha = request.form.get("cancha")
        
        if validar_turno(canchas_con_turnos, horario, cancha) == False:
            flash("El turno seleccionado no está disponible", "error")
            return redirect(url_for("turno.reservar", fecha=fecha))
        try:
            Turno.create(horario, fecha, cancha, 1)
            flash("Turno reservado con éxito", "success")
            return redirect(url_for("turno.index"))
        except ValueError as e:
            flash(str(e), "error")
            return redirect(url_for("turno.reservar", fecha=fecha))
    return render_template("turnos/reservar.html", fecha=fecha, canchas_con_turnos = canchas_con_turnos)


def canchas_con_turnos_disponibles(fecha):
    canchas = Cancha.get_all()
    canchas_con_turnos = []
    for cancha in canchas:
        turnos = Turno.get_turno_fecha_cancha(fecha,cancha.id)
        horarios_reservados = [turno.horario for turno in turnos]
        horarios_disponibles = [(horario.name, horario.value) for horario in Horario if horario not in horarios_reservados]
        canchas_con_turnos.append({
            "cancha": cancha,
            "turnos": horarios_disponibles
        })
    return canchas_con_turnos

def validar_turno(canchas_con_turnos, horario, cancha):
    for item in canchas_con_turnos:
            if str(item['cancha'].id) == cancha:
                if horario not in [turno[1] for turno in item['turnos']]:
                    return False
    return True
