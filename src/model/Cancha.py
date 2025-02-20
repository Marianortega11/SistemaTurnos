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
    
    
    def __repr__(self):
        return f"<Cancha {self.id} - {self.numero}>"
    
    @classmethod
    def create(cls,numero):
        cancha = cls(numero=numero)
        db.session.add(cancha)
        db.session.commit()
        return cancha

    @classmethod
    def delete(cls,id):
        cancha = cls.query.get(id)
        db.session.delete(cancha)
        db.session.commit()
        return cancha
    
    @classmethod
    def get_cancha(cls, numero):
        return cls.query.get(numero)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    