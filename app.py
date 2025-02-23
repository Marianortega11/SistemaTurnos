from src.web._init_ import create_app
from config.config import Config
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="static")

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

app = create_app(Config)

if __name__ == "__main__":
    app.run()
