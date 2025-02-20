from datetime import datetime;
from config.database import db;


    
class Cancha(db.Model):
    """
    Modelo de base de datos para representar una cancha.
    """
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    turnos = db.relationship("Turno", back_populates="cancha")
    
    
    @classmethod
    def create(cls,numero):
        cancha = cls(numero=numero)
        db.session.add(cancha)
        db.session.commit()
        return cancha
