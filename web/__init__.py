from flask import Flask

def create_app():
    """creates Flask instance"""
    app = Flask(__name__)

    return app
