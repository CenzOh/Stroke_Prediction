from distutils.log import Log
from urllib import request
from PyQt5.QtCore import Qt
from functools import partial
from Uiapp import Ui_MainWindow
from PyQt5 import QtCore, QtGui
import requests
import json
from PyQt5 import QtWidgets


class Login:
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def init(self):
        pass

    def buttons_actions(self):
        self.ui.login_pushButton.clicked.connect(
            partial(
                Login.login_handler, self
            )
        )
        self.ui.go_registration_pushButton.clicked.connect(
            partial(
                Login.go_registration_page, self
            )
        )

    def login_handler(self):
        username = self.ui.username_login_lineEdit.text()
        password = self.ui.password_login_lineEdit.text()
        if username != "" and password != "":
            x = requests.get('http://localhost:5000/app/login', json={
                "username": username,
                "password": password
            })
           
            if x.json()['res']:
                self.ui.Allpages.setCurrentIndex(2)
            else :
                print('login error ')
                Login.dialogue_message(self , 'Attention' , 'Login error password or username not valid ' )
        else:
            Login.dialogue_message(self , 'Attention' , 'Login error password or username not valid ' )

    def go_registration_page(self):
        self.ui.Allpages.setCurrentIndex(1)
    

    def dialogue_message(self , titel ,  body_message , status = 0) : 
        self.dialogue()
        self.layoutSTACK.addWidget(self.ui.widget_main)
        self.layoutSTACK.addWidget(self.verticalWidget)
        self.widgetSTACK = QtWidgets.QWidget()
        self.widgetSTACK.setLayout(self.layoutSTACK)
        self.setCentralWidget(self.widgetSTACK)
        self.bodymessage.setText(body_message)
        self.titeldialgue.setText(titel)
        self.redbutton.clicked.connect(partial(Login.close_dialogue , self ))
        self.greenbutton.hide()
        self.redbutton.setText('Okay')
        # 1 == conformation (yes or No ) , 2 == information (one button 'okay ')
        # if statu == 1 : 
        #     self.greenbutton.clicked.connect(partial(Adduser.confirmAdding , self ))
        # else : 
        #     self.greenbutton.hide()
        #     self.redbutton.setText('Okay')

    def close_dialogue(self): 
        self.layoutSTACK.removeWidget(self.verticalWidget)

