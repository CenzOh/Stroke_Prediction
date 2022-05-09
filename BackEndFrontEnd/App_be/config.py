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

class PridictionsHistory(db.Model):
    pridiction_id = db.Column(db.Integer,primary_key=True)
    avg_gluscose_level = db.Column(db.String(100),nullable=True)
    bmi = db.Column(db.String(100),nullable=True)
    stroke = db.Column(db.Integer,nullable=True)
    date = db.Column(db.String(100),nullable=True)
    user_id = db.Column(db.ForeignKey('user.id'))


db.create_all()