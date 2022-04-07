from PyQt5.QtCore import Qt
from functools import partial
from Uiapp import Ui_MainWindow
from PyQt5 import QtCore, QtGui
import requests
from pages.Login import Login

class Settings:
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def init(self):
        pass

    def buttons_actions(self):
       self.ui.change_username.clicked.connect(
           partial(
               Settings.change_username_handler, self
           )
       )

       self.ui.logOut.clicked.connect(
           partial(
               Settings.out_out_handler, self
           )
       )

    def change_username_handler(self):
        print("test")


    def out_out_handler(self):
        self.ui.Allpages.setCurrentIndex(0)