# test if the database file json exists
import os
import json


def registration(username, password):
    # if the file exists we get all users then append the new user
    if os.path.isfile('database/users.json'):
        with open('database/users.json', 'r') as openfile:
            # Reading from json file
            dictionary = json.load(openfile)
    # if the file does not exist we creat a new dict object the append the new user
    else:
        alluser = []
        dictionary = {

            "users": alluser
        }
    # add the new user 
    dictionary['users'].append(
        {
                "username": username,
                "password": password
        }
    )
    with open("database/users.json", "w") as outfile:
        json.dump(dictionary, outfile , indent= 4)


def login(username , password) :
    if os.path.isfile('database/users.json'):
        with open('database/users.json', 'r') as openfile:
            # Reading from json file
            dictionary = json.load(openfile)
        for user in dictionary.get('users'):
            if user.get('username') == username and user.get('password') == password :
                return True
        return False
    else :
        return False


def user_exist(username) :
    if os.path.isfile('database/users.json'):
        with open('database/users.json', 'r') as openfile:
            # Reading from json file
            dictionary = json.load(openfile)
        for user in dictionary.get('users'):
            if user.get('username') == username :
                return True
        return False
    else :
        return False


