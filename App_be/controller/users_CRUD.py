import json
from flask import Blueprint
from flask import request
from flask import jsonify
from httplib2 import Response

from App_be.controller.login_registration import registration , login , user_exist
users_crud = Blueprint('users_crud', __name__)

@users_crud.route('/app/login', methods=['GET'])
def get_user():
    req_data = request.json
    username = req_data['username']
    password = req_data['password']
    response = {
        "res" : login(username ,password)
    }
    return jsonify(response)


@users_crud.route('/app/adduser', methods=['POST'])
def add_entity_recursive():
    req_data = request.json
    username = req_data['username']
    password = req_data['password']

    if not user_exist(username):
        # usern does not exist add user 
        registration(username , password)
        response_data = {
            "res" : True
        }
    else : 
        # user exists 
        response_data = {
            "res" : False
        }

    return jsonify(response_data)
