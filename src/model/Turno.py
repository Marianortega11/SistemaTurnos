from datetime import datetime;
from config.database import db;


    
class Turno(db.Model):
    """
    Modelo de base de datos para representar un domicilio.
    """
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Time, nullable=True)
    fecha = db.Column(db.Date, nullable=True)
    cancha_id = db.Column(db.Integer, db.ForeignKey('cancha.id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    
    cancha = db.relationship("Cancha", back_populates="turnos")
    usuario = db.relationship("Usuario", back_populates="turnos")
    
    def __repr__(self):
        return f"<Turno {self.id} - {self.horario} - {self.cancha} - {self.usuario}>"
    
    @classmethod
    def create(cls,horario, fecha, cancha_id, usuario_id):
        turno = cls(horario=horario, fecha=fecha, cancha_id=cancha_id, usuario_id=usuario_id)
        db.session.add(turno)
        db.session.commit()
        return turno
        