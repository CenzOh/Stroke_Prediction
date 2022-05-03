import json
from flask import Blueprint
from flask import request
from flask import jsonify
from httplib2 import Response
from App_be.config import db, User

users_crud = Blueprint('users_crud', __name__)

@users_crud.route('/app/login', methods=['GET'])
def get_user():
    req_data = request.json
    username = req_data['username']
    password = req_data['password']
    user = User.query.filter_by(username=username, password=password).first()
    return jsonify( {"res":(user is not None)} )


@users_crud.route('/app/adduser', methods=['POST'])
def add_entity_recursive():
    req_data = request.json
    username = req_data['username']
    password = req_data['password']
    name = "unknown"
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"res": False})
    user = User(username=username, password=password, name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"res": True})
