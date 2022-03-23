#good file
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog): #login page
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self) #open login.ui when we call the fcn
        self.loginbutton.clicked.connect(self.loginfunction) #objs in the ui are now referencable
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) #hide the password with dots
        self.createaccountbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        username = self.username.text() #grab text from username field
        password = self.password.text()
        print("Successfully logged in with username: ", username, "and password: ", password)

    def gotocreate(self): #after clicking the create account push button go to create account page
        createaccount = CreateAcc() #new instance
        widget.addWidget(createaccount)
        widget.setCurrentIndex(widget.currentIndex()+1) #increment widget in the stack to go between pages

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createaccount.ui",self) #go to the createaccount ui
        self.signupbutton.clicked.connect(self.createaccount) #clicking signup button
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)


    def createaccount(self):
        username = self.username.text()
        if self.password.text() == self.confirmpassword.text(): #both password fields are equal
            password = self.password.text()
            print("Sucessfully created account with username: ", username, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget() #increment index to change screen, from login to create account,etc.
widget.addWidget(mainwindow)
widget.setFixedWidth(500) #user cant change size
widget.setFixedHeight(700)
widget.show()
app.exec_()