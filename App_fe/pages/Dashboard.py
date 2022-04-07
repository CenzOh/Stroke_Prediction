from PyQt5.QtCore import Qt
from functools import partial
from Uiapp import Ui_MainWindow
from PyQt5 import QtCore, QtGui
import requests
from pages.Login import Login

class Dashboard:
    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def buttons_actions(self):
        self.ui.prediction_button.clicked.connect(
            partial(
                Dashboard.prediction_handler, self
            )
        )

        self.ui.logOut.clicked.connect(
            partial(
                Dashboard.out_out_handler, self
            )
        )

        self.ui.page_2.clicked.connect(partial(self.switch_page)) #go to settings page

    def switch_page(self): 
        if self.ui.page_2.isChecked():
            self.ui.LESPAGES.setCurrentIndex(1) 
            self.ui.Allpages.setCurrentIndex(3)


    def init(self):
        pass

    def prediction_handler(self):
        gender = self.ui.gender.currentIndex()
        age = self.ui.age.text()
        hypertension = self.ui.hypertension.currentIndex()
        heart_disease = self.ui.heart_disease.currentIndex()
        ever_married = self.ui.ever_married.currentIndex()
        work_type = self.ui.work_type.currentIndex()
        Residence_type = self.ui.Residence_type.currentIndex()
        avg_glucose_level = self.ui.avg_glucose_level.text()
        bmi = self.ui.bmi.text()
        smoking_status = self.ui.smoking_status.currentIndex()
        if age != "" and avg_glucose_level != "" and bmi != "":
            age = float(age)
            avg_glucose_level = float(avg_glucose_level)
            bmi = float(bmi)
            x = requests.get('http://localhost:5000/app/model', json={
                "gender": gender,
                "age": age,
                "hypertension": hypertension,
                "heart_disease":  heart_disease,
                "ever_married": ever_married,
                "work_type": work_type,
                "Residence_type": Residence_type,
                "avg_glucose_level": avg_glucose_level,
                "bmi": bmi,
                "smoking_status": smoking_status

            })
            if x.json()['res'] == 1 :
                Login.dialogue_message(self , 'Result' , 'The algorithm has predicted a Stroke' )
            elif x.json()['res'] == 0 :
                Login.dialogue_message(self , 'Result' , 'The algorithm has predicted No Stroke' )
        else : 
            Login.dialogue_message(self , 'Attention' , 'Error invalid inputs ' )


    def out_out_handler(self): #TEST, when user clicks button they will delete account
        # self.ui.Allpages.setCurrentIndex(0) #ORIGINAL CODE
        username = self.ui.username_login_lineEdit.text() #CURRENT ERROR - can not find URL?
        password = self.ui.password_login_lineEdit.text() #CHECK IF USER REGISTERED NEW ACCOUNT, NOTHING WOULD BE IN LOGIN **
        if username != "" and password != "":
            x = requests.post('http://localhost:5000/app/deleteuser', json={
                "username": username,
                "password": password
            })
            if x.json()['res']:
                self.ui.Allpages.setCurrentIndex(0) #delete user account and go back to login
            else :
                print('delete error ')
                Login.dialogue_message(self , 'Attention' , 'Something went wrong inner loop ' )
        else:
            print('delete error')
            Login.dialogue_message(self , 'Attention' , 'Something went wrong outer loop ' )

