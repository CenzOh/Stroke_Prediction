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


def delete_user_pass(username, password) : #user will remove their account from the database
    if os.path.isfile('database/users.json'):
        with open('database/users.json', 'r') as openfile: #r+ for read and write

            dictionary = json.load(openfile)
        for user in dictionary.get('users'):
            if user.get('username') == username and user.get('password') == password : #user exists, can delete
                user.pop('username', None)
                user.pop('password', None)
                # print(dictionary['users'].values())
                #del dictionary['users']["username": username]
                # ^ POTENTIAL PROBLEM STATEMENT
                with open("database/users.json", "w") as outfile:
                    json.dump(dictionary, outfile , indent= 4)

                return True
        return False
    else:
        return False