from src.model.Cancha import Cancha
from src.model.Usuario import Usuario
from src.model.Turno import Turno
from datetime import datetime
from config.database import db

def run():
    cancha = Cancha.create(numero = "1")
    cancha2 = Cancha.create(numero = "2")
    usuario = Usuario.create(email = "usuario1@gmail.com", password="asdasd")
