from datetime import datetime;
from config.database import db;
from flask_bcrypt import generate_password_hash;
from flask_bcrypt import check_password_hash;

    
class Usuario(db.Model):
    """
    Modelo de base de datos para representar un usuario.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    turnos = db.relationship("Turno", back_populates="usuario")
    
    
    @classmethod
    def create(cls,email, password):
        hashed_password = generate_password_hash(password)
        usuario = Usuario(email=email, password=hashed_password)
        db.session.add(usuario)
        db.session.commit()
        return usuario
    
    @classmethod
    def check_password(cls, email, password):
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            if check_password_hash(usuario.password, password):
                return usuario
        return False