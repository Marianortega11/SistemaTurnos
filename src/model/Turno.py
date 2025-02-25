from datetime import datetime

from enum import Enum;
from config.database import db;

class Horario(Enum):
    QUINCEHORAS = "15:00"
    DIECISEIS = "16:00"
    DIECISIETEHORAS = "17:00"
    DIECIOCHOHORAS = "18:00"
    DIECINUEVEHORAS = "19:00"
    VEINTEHORAS = "20:00"
    VEINTIUNAHORAS = "21:00"
    VEINTIDOSHORAS = "22:00"
    
    
class Turno(db.Model):
    """
    Modelo de base de datos para representar un domicilio.
    """
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Enum(Horario), nullable=True)
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
        horario = Horario(horario)
        if cls.check_duplicate(horario, fecha, cancha_id):
            raise ValueError("Turno ya reservado")
        turno = cls(horario=horario, fecha=fecha, cancha_id=cancha_id, usuario_id=usuario_id)
        db.session.add(turno)
        db.session.commit()
        return turno
    
    @classmethod
    def delete(cls,id):
        turno = cls.query.get(id)
        db.session.delete(turno)
        db.session.commit()
        return turno
    
    
    """
        a implementar
    """
    @classmethod
    def update(cls, id, horario, fecha, cancha_id, usuario_id):
       pass
    
    @classmethod
    def get_turno(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def check_duplicate(cls, horario, fecha, cancha_id):
        return cls.query.filter_by(horario=horario, fecha=fecha, cancha_id=cancha_id).first()
    
    @classmethod    
    def get_turno_fecha(cls, fecha):
        return cls.query.filter_by(fecha=fecha).all()
    
    @classmethod
    def get_turno_fecha_cancha(cls,fecha,cancha_id):
        return cls.query.filter_by(fecha=fecha, cancha_id=cancha_id).all()
        
        
        
    