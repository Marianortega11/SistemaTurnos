from src.model.Cancha import Cancha
from src.model.Usuario import Usuario
from src.model.Turno import Turno
from datetime import datetime
from config.database import db

def run():
    cancha = Cancha.create(numero = "1")
    usuario = Usuario.create(email = "usuario1@gmail.com")
    turno = Turno.create(datetime.now().time(),datetime.now().date(), cancha_id = cancha.id, usuario_id = usuario.id)
