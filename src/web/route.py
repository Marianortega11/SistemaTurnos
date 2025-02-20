from flask import Blueprint, render_template
from config.config import env
from config.database import db

def register(app):
    @app.route("/")
    def home():

        return render_template("index.html")



