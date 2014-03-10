from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
   
def create_app():
    """creates Flask instance"""
    app = Flask(__name__)

    return app

def create_db():
    db =  SQLAlchemy()
    return db
