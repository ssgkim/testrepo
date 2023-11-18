# app.py

from flask import Flask
from urllib.parse import quote

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return quote('Hello, World! This is a simple Flask app 12333.')

    return app
