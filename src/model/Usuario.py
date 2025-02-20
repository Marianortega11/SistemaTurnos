from datetime import datetime;
from config.database import db;


    
class Usuario(db.Model):
    """
    Modelo de base de datos para representar un usuario.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    turnos = db.relationship("Turno", back_populates="usuario")
    
    
    @classmethod
    def create(cls,email):
        usuario = cls(email=email)
        db.session.add(usuario)
        db.session.commit()
        return usuario