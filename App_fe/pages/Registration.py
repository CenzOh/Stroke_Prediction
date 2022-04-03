from PyQt5.QtCore import Qt
from functools import partial
from Uiapp import Ui_MainWindow
from PyQt5 import QtCore , QtGui
import requests
import json
from pages.Login import Login

class Registration:
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def init(self):
        pass


    def buttons_actions(self):
        self.ui.register_pushButton.clicked.connect(
            partial(
                Registration.registration_handler , self 
            )
        )
        self.ui.go_login_pushButton.clicked.connect(
            partial(
                Registration.go_login_page , self 
            )
        )
    
    def registration_handler(self):
        username = self.ui.username_registration_lineEdit.text()
        password = self.ui.password_registration_lineEdit.text()
        if username != "" and password != "" :
            x = requests.post('http://localhost:5000/app/adduser', json={
                "username": username,
                "password": password
            })
            if x.json()['res'] : 
                self.ui.Allpages.setCurrentIndex(2)
            else : 
                print('this user exists !')
                Login.dialogue_message(self , 'Attention' , 'This user exists' )
        else :
            print('Registration error !')
            Login.dialogue_message(self , 'Attention' , 'Registration error password or username not valid ' )
    

    def go_login_page(self):
        self.ui.Allpages.setCurrentIndex(0)
