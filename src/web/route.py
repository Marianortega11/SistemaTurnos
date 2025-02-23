from flask import Blueprint, render_template
from config.config import env
from config.database import db
from src.web.controllers.turno import bp as turno_bp
from src.web.controllers.auth import bp as auth_bp
from config import config
def register(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    app.register_blueprint(turno_bp)
    app.register_blueprint(auth_bp)


