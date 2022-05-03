from flask_sqlalchemy import SQLAlchemy
from flask import Flask

application = Flask(__name__,)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sql'
application.secret_key = 'this is a secret'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(100), default='profile.png')
    password = db.Column(db.String(100))
    stroke = db.Column(db.Integer, default=-1)

db.create_all()