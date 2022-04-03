# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIviews\Uiapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.widget_main.setObjectName("widget_main")
        self.THEAPPLICATIONCHILD = QtWidgets.QVBoxLayout(self.widget_main)
        self.THEAPPLICATIONCHILD.setContentsMargins(0, 0, 0, 0)
        self.THEAPPLICATIONCHILD.setSpacing(0)
        self.THEAPPLICATIONCHILD.setObjectName("THEAPPLICATIONCHILD")
        self.Allpages = QtWidgets.QStackedWidget(self.widget_main)
        self.Allpages.setStyleSheet("background-color : white")
        self.Allpages.setObjectName("Allpages")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.loginPage)
        self.verticalLayout_4.setContentsMargins(100, 100, 100, 100)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalWidget_2 = QtWidgets.QWidget(self.loginPage)
        self.verticalWidget_2.setStyleSheet("\n"
"QPushButton{ \n"
"background-color: rgb(56, 180, 116)  ;\n"
"border-radius: 8px;\n"
"color : white ;\n"
"border: none;\n"
"font: 87 9pt \"Montserrat Black\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(56, 180, 116 , 100)  ;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgba(56, 180, 116, 255) ;\n"
"border-radius: 3px;\n"
"color : white ;\n"
"border:2px solid  rgba(56, 180, 116, 100);\n"
"padding-left: 12px;\n"
"padding-top : 7px ;\n"
"padding-bottom : 7px ;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid  rgba(56, 180, 116, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid  rgba(56, 180, 116, 255) ;\n"
"    \n"
"}")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setContentsMargins(80, 80, 80, 80)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_3.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"background-color : transparent ")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.username_login_lineEdit = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.username_login_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.username_login_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.username_login_lineEdit.setObjectName("username_login_lineEdit")
        self.verticalLayout_3.addWidget(self.username_login_lineEdit)
        self.password_login_lineEdit = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.password_login_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.password_login_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.password_login_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_login_lineEdit.setObjectName("password_login_lineEdit")
        self.verticalLayout_3.addWidget(self.password_login_lineEdit)
        self.login_pushButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.login_pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.login_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.login_pushButton.setObjectName("login_pushButton")
        self.verticalLayout_3.addWidget(self.login_pushButton)
        self.go_registration_pushButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.go_registration_pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.go_registration_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.go_registration_pushButton.setObjectName("go_registration_pushButton")
        self.verticalLayout_3.addWidget(self.go_registration_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.verticalWidget_2)
        self.Allpages.addWidget(self.loginPage)
        self.registrationPage = QtWidgets.QWidget()
        self.registrationPage.setObjectName("registrationPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.registrationPage)
        self.verticalLayout_2.setContentsMargins(100, 100, 100, 100)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget = QtWidgets.QWidget(self.registrationPage)
        self.verticalWidget.setStyleSheet("\n"
"\n"
"QPushButton{ \n"
"background-color: rgb(56, 180, 116)  ;\n"
"border-radius: 8px;\n"
"color : white ;\n"
"border: none;\n"
"font: 87 9pt \"Montserrat Black\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(56, 180, 116 , 100)  ;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgba(56, 180, 116, 255) ;\n"
"border-radius: 3px;\n"
"color : white ;\n"
"border:2px solid  rgba(56, 180, 116, 100);\n"
"padding-left: 12px;\n"
"padding-top : 7px ;\n"
"padding-bottom : 7px ;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid  rgba(56, 180, 116, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid  rgba(56, 180, 116, 255) ;\n"
"    \n"
"}")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(80, 80, 80, 80)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"background-color : transparent")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.username_registration_lineEdit = QtWidgets.QLineEdit(self.verticalWidget)
        self.username_registration_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.username_registration_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.username_registration_lineEdit.setObjectName("username_registration_lineEdit")
        self.verticalLayout.addWidget(self.username_registration_lineEdit)
        self.password_registration_lineEdit = QtWidgets.QLineEdit(self.verticalWidget)
        self.password_registration_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.password_registration_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.password_registration_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_registration_lineEdit.setObjectName("password_registration_lineEdit")
        self.verticalLayout.addWidget(self.password_registration_lineEdit)
        self.register_pushButton = QtWidgets.QPushButton(self.verticalWidget)
        self.register_pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.register_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.register_pushButton.setObjectName("register_pushButton")
        self.verticalLayout.addWidget(self.register_pushButton)
        self.go_login_pushButton = QtWidgets.QPushButton(self.verticalWidget)
        self.go_login_pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.go_login_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.go_login_pushButton.setObjectName("go_login_pushButton")
        self.verticalLayout.addWidget(self.go_login_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.verticalWidget)
        self.Allpages.addWidget(self.registrationPage)
        self.dashBoardPage = QtWidgets.QWidget()
        self.dashBoardPage.setObjectName("dashBoardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dashBoardPage)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LESPAGES = QtWidgets.QStackedWidget(self.dashBoardPage)
        self.LESPAGES.setStyleSheet("QScrollArea{\n"
"border : none;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color : white;\n"
"font: 10pt \"Montserrat\";\n"
"color : white;\n"
"\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: transparent;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 0px 21px 0 21px;\n"
"      border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #7E73FF ;\n"
"    min-width: 25px;\n"
"     border-radius: 5px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: transparent;\n"
"}\n"
" QScrollBar:vertical {\n"
"       border: none;\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 21px 0 21px 0;\n"
"       border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical { \n"
"       background: #7E73FF ;\n"
"        min-height: 25px;\n"
"       border-radius: 5px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 20px;\n"
"       border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"       border: none;\n"
"    background: transparent;\n"
"     height: 20px;\n"
"       border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QTableWidget {\n"
"    border : none ; \n"
"    font-size: 8pt;\n"
"     background-color: rgba(255, 255, 255,255);\n"
"    alternate-background-color: rgba(255, 255, 255, 255);\n"
"    color : Black;\n"
"    font: 8pt \"Montserrat\";\n"
"   border-radius: 8px;\n"
"   \n"
"}\n"
"      \n"
"QHeaderView::section {\n"
"    background-color: rgb(79, 79, 79);\n"
"    padding: 4px;\n"
"    border: none;\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    color : white ;\n"
"}\n"
"\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color:  rgb(79, 79, 79);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"border-radius: 5px;\n"
"color :white  ;\n"
"border: 0px solid #2f3939;\n"
"padding-left: 12px;\n"
"padding-right: 12px;\n"
"padding-top : 7px ;\n"
"padding-bottom : 7px ;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background-color : rgba(56, 180, 116 , 255) ;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"      subcontrol-origin: padding;\n"
"    subcontrol-position: top left;\n"
"    border-left-width: 0px;\n"
"    border-left-style: solid; /* just a single line */\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgba(56, 180, 116 ,100) ;\n"
"    color: white;\n"
"    background-color:rgba(56, 180, 116 , 70); \n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/image/DownArrow_white.png);\n"
"     width: 10px; \n"
"     height: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{ \n"
"background-color: #7E73FF  ;\n"
"border-radius: 8px;\n"
"color : white ;\n"
"border: none;\n"
"    font: 87 9pt \"Montserrat Black\";\n"
"\n"
" }\n"
"QPushButton:hover{\n"
"background-color: rgba(126, 115, 255, 100)  ;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgba(126, 115, 255, 255) ;\n"
"border-radius: 3px;\n"
"color : white ;\n"
"border:2px solid  rgba(126, 115, 255, 100);\n"
"padding-left: 12px;\n"
"padding-top : 7px ;\n"
"padding-bottom : 7px ;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid  rgba(126, 115, 255, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid   rgba(126, 115, 255, 255) ;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.LESPAGES.setObjectName("LESPAGES")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalWidget_3 = QtWidgets.QWidget(self.page)
        self.verticalWidget_3.setMinimumSize(QtCore.QSize(641, 751))
        self.verticalWidget_3.setMaximumSize(QtCore.QSize(641, 751))
        self.verticalWidget_3.setStyleSheet("\n"
"QPushButton{ \n"
"background-color: rgb(56, 180, 116)  ;\n"
"border-radius: 8px;\n"
"color : white ;\n"
"border: none;\n"
"font: 87 9pt \"Montserrat Black\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(56, 180, 116 , 100)  ;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgba(56, 180, 116, 255) ;\n"
"border-radius: 3px;\n"
"color : white ;\n"
"border:2px solid  rgba(56, 180, 116, 100);\n"
"padding-left: 12px;\n"
"padding-top : 7px ;\n"
"padding-bottom : 7px ;\n"
"    font: 10pt \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid  rgba(56, 180, 116, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid  rgba(56, 180, 116, 255) ;\n"
"    \n"
"}")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_6.setContentsMargins(80, 10, 80, 80)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_4.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"background-color : transparent ")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_5.setStyleSheet("color : black ")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gender = QtWidgets.QComboBox(self.verticalWidget_3)
        self.gender.setMinimumSize(QtCore.QSize(200, 35))
        self.gender.setMaximumSize(QtCore.QSize(200, 35))
        self.gender.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.horizontalLayout_2.addWidget(self.gender)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_7.setStyleSheet("color : black ")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.age = QtWidgets.QLineEdit(self.verticalWidget_3)
        self.age.setMinimumSize(QtCore.QSize(200, 35))
        self.age.setMaximumSize(QtCore.QSize(200, 35))
        self.age.setObjectName("age")
        self.horizontalLayout_3.addWidget(self.age)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_10.setStyleSheet("color : black ")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.hypertension = QtWidgets.QComboBox(self.verticalWidget_3)
        self.hypertension.setMinimumSize(QtCore.QSize(200, 35))
        self.hypertension.setMaximumSize(QtCore.QSize(200, 35))
        self.hypertension.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hypertension.setObjectName("hypertension")
        self.hypertension.addItem("")
        self.hypertension.addItem("")
        self.horizontalLayout_6.addWidget(self.hypertension)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_11.setStyleSheet("color : black ")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.heart_disease = QtWidgets.QComboBox(self.verticalWidget_3)
        self.heart_disease.setMinimumSize(QtCore.QSize(200, 35))
        self.heart_disease.setMaximumSize(QtCore.QSize(200, 35))
        self.heart_disease.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.heart_disease.setObjectName("heart_disease")
        self.heart_disease.addItem("")
        self.heart_disease.addItem("")
        self.horizontalLayout_7.addWidget(self.heart_disease)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_12.setStyleSheet("color : black ")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.ever_married = QtWidgets.QComboBox(self.verticalWidget_3)
        self.ever_married.setMinimumSize(QtCore.QSize(200, 35))
        self.ever_married.setMaximumSize(QtCore.QSize(200, 35))
        self.ever_married.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ever_married.setObjectName("ever_married")
        self.ever_married.addItem("")
        self.ever_married.addItem("")
        self.horizontalLayout_8.addWidget(self.ever_married)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_13.setStyleSheet("color : black ")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.work_type = QtWidgets.QComboBox(self.verticalWidget_3)
        self.work_type.setMinimumSize(QtCore.QSize(200, 35))
        self.work_type.setMaximumSize(QtCore.QSize(200, 35))
        self.work_type.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.work_type.setObjectName("work_type")
        self.work_type.addItem("")
        self.work_type.addItem("")
        self.work_type.addItem("")
        self.work_type.addItem("")
        self.work_type.addItem("")
        self.horizontalLayout_9.addWidget(self.work_type)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_14.setStyleSheet("color : black ")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.Residence_type = QtWidgets.QComboBox(self.verticalWidget_3)
        self.Residence_type.setMinimumSize(QtCore.QSize(200, 35))
        self.Residence_type.setMaximumSize(QtCore.QSize(200, 35))
        self.Residence_type.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Residence_type.setObjectName("Residence_type")
        self.Residence_type.addItem("")
        self.Residence_type.addItem("")
        self.horizontalLayout_10.addWidget(self.Residence_type)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_15.setStyleSheet("color : black ")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.avg_glucose_level = QtWidgets.QLineEdit(self.verticalWidget_3)
        self.avg_glucose_level.setMinimumSize(QtCore.QSize(200, 35))
        self.avg_glucose_level.setMaximumSize(QtCore.QSize(200, 35))
        self.avg_glucose_level.setObjectName("avg_glucose_level")
        self.horizontalLayout_11.addWidget(self.avg_glucose_level)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_16.setStyleSheet("color : black ")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.bmi = QtWidgets.QLineEdit(self.verticalWidget_3)
        self.bmi.setMinimumSize(QtCore.QSize(200, 35))
        self.bmi.setMaximumSize(QtCore.QSize(200, 35))
        self.bmi.setObjectName("bmi")
        self.horizontalLayout_12.addWidget(self.bmi)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_17.setStyleSheet("color : black ")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_13.addWidget(self.label_17)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.smoking_status = QtWidgets.QComboBox(self.verticalWidget_3)
        self.smoking_status.setMinimumSize(QtCore.QSize(200, 35))
        self.smoking_status.setMaximumSize(QtCore.QSize(200, 35))
        self.smoking_status.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.smoking_status.setObjectName("smoking_status")
        self.smoking_status.addItem("")
        self.smoking_status.addItem("")
        self.smoking_status.addItem("")
        self.smoking_status.addItem("")
        self.horizontalLayout_13.addWidget(self.smoking_status)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.prediction_button = QtWidgets.QPushButton(self.verticalWidget_3)
        self.prediction_button.setMinimumSize(QtCore.QSize(0, 35))
        self.prediction_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.prediction_button.setObjectName("prediction_button")
        self.verticalLayout_6.addWidget(self.prediction_button)
        self.logOut = QtWidgets.QPushButton(self.verticalWidget_3)
        self.logOut.setMinimumSize(QtCore.QSize(200, 35))
        self.logOut.setMaximumSize(QtCore.QSize(200, 35))
        self.logOut.setObjectName("logOut")
        self.verticalLayout_6.addWidget(self.logOut, 0, QtCore.Qt.AlignRight)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem14)
        self.gridLayout_9.addWidget(self.verticalWidget_3, 0, 0, 1, 1)
        self.LESPAGES.addWidget(self.page)
        self.gridLayout_4.addWidget(self.LESPAGES, 0, 1, 1, 1)
        self.verticalWidget_panal = QtWidgets.QWidget(self.dashBoardPage)
        self.verticalWidget_panal.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalWidget_panal.setMaximumSize(QtCore.QSize(200, 16777215))
        self.verticalWidget_panal.setStyleSheet("background-color :rgb(56 , 180 , 116) ;\n"
"\n"
"font: 8.5pt \"Segoe UI\";\n"
"")
        self.verticalWidget_panal.setObjectName("verticalWidget_panal")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_panal)
        self.verticalLayout_5.setContentsMargins(0, 12, 0, 17)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem15)
        self.label = QtWidgets.QLabel(self.verticalWidget_panal)
        self.label.setStyleSheet("font: 81 16pt \"Montserrat ExtraBold\";\n"
"color : white ;")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem16 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem16)
        self.appname = QtWidgets.QLabel(self.verticalWidget_panal)
        self.appname.setStyleSheet("color : #858585 ;")
        self.appname.setText("")
        self.appname.setAlignment(QtCore.Qt.AlignCenter)
        self.appname.setObjectName("appname")
        self.verticalLayout_5.addWidget(self.appname)
        self.page_1 = QtWidgets.QRadioButton(self.verticalWidget_panal)
        self.page_1.setMinimumSize(QtCore.QSize(200, 50))
        self.page_1.setMaximumSize(QtCore.QSize(200, 50))
        self.page_1.setStyleSheet("QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"Text-align:centre;\n"
"padding-left : 18px;\n"
"color : white;\n"
"font: 8pt \"Montserrat\";\n"
" }\n"
"\n"
"QRadioButton::checked {\n"
"background-color :  qlineargradient(spread:pad, x1:0.476, y1:0.0626364, x2:0.477273, y2:0.885, stop:0 rgba(255, 255, 255, 150), stop:1 rgba(255, 255, 255, 100))\n"
"  \n"
" }\n"
"\n"
"QRadioButton::indicator {\n"
"  width:                  0px;\n"
"  height:                 0px;\n"
" border-radius:          0px;\n"
" }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/chart/line-chart-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page_1.setIcon(icon1)
        self.page_1.setIconSize(QtCore.QSize(25, 25))
        self.page_1.setChecked(True)
        self.page_1.setObjectName("page_1")
        self.verticalLayout_5.addWidget(self.page_1)
        self.page_2 = QtWidgets.QRadioButton(self.verticalWidget_panal)
        self.page_2.setMinimumSize(QtCore.QSize(200, 50))
        self.page_2.setMaximumSize(QtCore.QSize(200, 50))
        self.page_2.setStyleSheet("QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"Text-align:centre;\n"
"padding-left : 18px;\n"
"color : white;\n"
"font: 8pt \"Montserrat\";\n"
" }\n"
"\n"
"QRadioButton::checked {\n"
"background-color :  qlineargradient(spread:pad, x1:0.476, y1:0.0626364, x2:0.477273, y2:0.885, stop:0 rgba(255, 255, 255, 150), stop:1 rgba(255, 255, 255, 100))\n"
"  \n"
" }\n"
"\n"
"QRadioButton::indicator {\n"
"  width:                  0px;\n"
"  height:                 0px;\n"
" border-radius:          0px;\n"
" }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/core/settings-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page_2.setIcon(icon2)
        self.page_2.setIconSize(QtCore.QSize(25, 25))
        self.page_2.setChecked(False)
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5.addWidget(self.page_2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem17)
        self.gridLayout_4.addWidget(self.verticalWidget_panal, 0, 0, 1, 1)
        self.Allpages.addWidget(self.dashBoardPage)
        self.THEAPPLICATIONCHILD.addWidget(self.Allpages)
        self.gridLayout.addWidget(self.widget_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Allpages.setCurrentIndex(0)
        self.LESPAGES.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.username_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Username ..."))
        self.password_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Password ..."))
        self.login_pushButton.setText(_translate("MainWindow", "Login"))
        self.go_registration_pushButton.setText(_translate("MainWindow", "Go to registration  page"))
        self.label_2.setText(_translate("MainWindow", "Registration"))
        self.username_registration_lineEdit.setPlaceholderText(_translate("MainWindow", "Username ..."))
        self.password_registration_lineEdit.setPlaceholderText(_translate("MainWindow", "Password ..."))
        self.register_pushButton.setText(_translate("MainWindow", "Register user"))
        self.go_login_pushButton.setText(_translate("MainWindow", "Go to login page "))
        self.label_4.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "gender "))
        self.gender.setItemText(0, _translate("MainWindow", "Female"))
        self.gender.setItemText(1, _translate("MainWindow", "Male"))
        self.gender.setItemText(2, _translate("MainWindow", "Other"))
        self.label_7.setText(_translate("MainWindow", "age"))
        self.label_10.setText(_translate("MainWindow", "hypertension"))
        self.hypertension.setItemText(0, _translate("MainWindow", "No"))
        self.hypertension.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_11.setText(_translate("MainWindow", "heart_disease"))
        self.heart_disease.setItemText(0, _translate("MainWindow", "No"))
        self.heart_disease.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_12.setText(_translate("MainWindow", "ever_married"))
        self.ever_married.setItemText(0, _translate("MainWindow", "No"))
        self.ever_married.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_13.setText(_translate("MainWindow", "work_type"))
        self.work_type.setItemText(0, _translate("MainWindow", "Govt_job"))
        self.work_type.setItemText(1, _translate("MainWindow", "Never_worked"))
        self.work_type.setItemText(2, _translate("MainWindow", "Private"))
        self.work_type.setItemText(3, _translate("MainWindow", "Self-employed"))
        self.work_type.setItemText(4, _translate("MainWindow", "children"))
        self.label_14.setText(_translate("MainWindow", "Residence_type"))
        self.Residence_type.setItemText(0, _translate("MainWindow", "Rural"))
        self.Residence_type.setItemText(1, _translate("MainWindow", "Urban"))
        self.label_15.setText(_translate("MainWindow", "avg_glucose_level"))
        self.label_16.setText(_translate("MainWindow", "bmi"))
        self.label_17.setText(_translate("MainWindow", "smoking_status"))
        self.smoking_status.setItemText(0, _translate("MainWindow", "Unknown"))
        self.smoking_status.setItemText(1, _translate("MainWindow", "formerly smoked"))
        self.smoking_status.setItemText(2, _translate("MainWindow", "never smoked"))
        self.smoking_status.setItemText(3, _translate("MainWindow", "smokes"))
        self.prediction_button.setText(_translate("MainWindow", "Predict"))
        self.logOut.setText(_translate("MainWindow", "log out"))
        self.label.setText(_translate("MainWindow", "APP"))
        self.page_1.setText(_translate("MainWindow", "  Dashboard"))
        self.page_2.setText(_translate("MainWindow", "  Settings"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
