from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SubmitField
from wtforms.validators import ValidationError, InputRequired
from src.model.Turno import Horario

class FechaForm(FlaskForm):
    def validate_fecha_turno(form, field):
        if field.data is None:
            raise ValidationError("La fecha del turno es obligatoria.")
        if field.data <= datetime.today().date():
            raise ValidationError("La fecha del turno no puede ser menor a la de hoy")
        
    fecha = DateField("Fecha", validators=[InputRequired(message="La fecha del turno es obligatoria."), validate_fecha_turno], render_kw={"placeholder": "fecha"})
    submit = SubmitField("Seleccionar Fecha")

