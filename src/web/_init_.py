from flask import Flask
from flask_session import Session
from config import database
from config.database import db
from src.web import command, route
    
session = Session()

def create_app(config_class):
    app = Flask(__name__)
    
    command.register(app)

    app.config.from_object(config_class)


    route.register(app)

    database.init_app(app)
    session.init_app(app)
    with app.app_context():
        db.create_all() 

    return app
