from PyQt5.QtGui import QColor, QIcon, QPainter, QPixmap
from PyQt5 import QtCore , Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication , QGraphicsDropShadowEffect , QStackedLayout
from functools import partial
import sys
from Uiapp import Ui_MainWindow
from PyQt5 import QtWidgets
from pages.Dashboard import Dashboard
from pages.Registration import Registration
from pages.Login import Login
from pages.Settings import Settings


class MainWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # add shadow to left bar widget , the widgets in the first page
        self.shadowUi(self.ui.verticalWidget_panal)
        self.shadowUi(self.ui.verticalWidget_2)
        self.shadowUi(self.ui.verticalWidget)
        self.layoutSTACK = QStackedLayout()
        self.layoutSTACK.setStackingMode(QStackedLayout.StackAll)

        # Change the color of the left bar's icons
        self.ui.page_1.setIcon(self.QIcon_from_svg(
            ":/image/chart/line-chart-solid.svg"))
        self.ui.page_2.setIcon(self.QIcon_from_svg(
            ":/image/core/settings-solid.svg"))


        # import all pages 
        Dashboard.buttons_actions(self)
        Dashboard.init(self)

        Login.buttons_actions(self)
        Login.init(self)

        Registration.buttons_actions(self)
        Registration.init(self)

        #Settings.buttons_actions(self)
        #Settings.init(self)

    
    def buttons_actions(self):
        self.ui.page_1.clicked.connect(partial(self.switch_page))
        self.ui.page_2.clicked.connect(partial(self.switch_page))
        
    def switch_page(self):
        if self.ui.page_1.isChecked():
            self.ui.LESPAGES.setCurrentIndex(0)
            
        elif self.ui.page_2.isChecked():
            self.ui.LESPAGES.setCurrentIndex(1)
            # self.ui.Allpages.setCurrentIndex(3)
    

    def QIcon_from_svg(self, svg_filepath):
        img = QPixmap(svg_filepath)
        qp = QPainter(img)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.fillRect(img.rect(), QColor(255, 255, 255))
        qp.end()
        return QIcon(img)

    def shadowUi(self, Widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 50))
        Widget.setGraphicsEffect(shadow)
    

    def dialogue(self):
        self.verticalWidget = QtWidgets.QWidget()
        self.verticalWidget.setStyleSheet(
            "background-color : rgba(0,0,0,100) ; ")
        self.verticalWidget.setObjectName("verticalWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalWidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(600, 0))
        self.verticalWidget_2.setStyleSheet("QWidget{\n"
                                            "background-color : rgb(35,35,35)  ;\n"
                                            "border-radius: 5px;\n"
                                            "border: 6px solid #2d3838;\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "QLable{\n"
                                            "color : white ; \n"
                                            "font: 12pt \"Segoe UI\";\n"
                                            "\n"
                                            "}")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titeldialgue = QtWidgets.QLabel(self.verticalWidget_2)
        self.titeldialgue.setStyleSheet("\n"
                                        "\n"
                                        "QLabel{\n"
                                        "font: 10pt \"Segoe UI\";\n"
                                        "color : white ;\n"
                                        "padding-left : 10px ;\n"
                                        "border : none ; \n"
                                        "\n"
                                        "}")
        self.titeldialgue.setObjectName("titeldialgue")
        self.verticalLayout_2.addWidget(self.titeldialgue)
        self.bodymessage = QtWidgets.QLabel(self.verticalWidget_2)
        self.bodymessage.setStyleSheet("QLabel{\n"
                                       "\n"
                                       "font: 10pt \"Segoe UI\";\n"
                                       "color : white ; \n"
                                       "background-color : #2d3838 ; \n"
                                       "border-radius: 5px;\n"
                                       "padding-left : 9px;\n"
                                       "padding-right : 9px;\n"
                                       "padding-top : 9px;\n"
                                       "padding-bottom : 20px;\n"
                                       "border : none ; \n"
                                       "}")
        self.bodymessage.setObjectName("bodymessage")
        self.verticalLayout_2.addWidget(self.bodymessage)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget_2)
        self.horizontalWidget.setStyleSheet("border : none ; ")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.greenbutton = QtWidgets.QPushButton(self.horizontalWidget)
        self.greenbutton.setMinimumSize(QtCore.QSize(148, 0))
        self.greenbutton.setStyleSheet("\n"
                                       "\n"
                                       "\n"
                                       "QPushButton{ \n"
                                       "background-color: rgba(56, 180, 116, 255);\n"
                                       "border-radius: 5px;\n"
                                       "color : white ;\n"
                                       "border: none;\n"
                                       "font: 12pt \"Segoe UI\";\n"
                                       "padding-top : 7px ;\n"
                                       "padding-bottom : 7px ;\n"
                                       "padding-right : 27px ;\n"
                                       "padding-left : 27px ;\n"
                                       " }\n"
                                       "QPushButton:hover{\n"
                                       "border: 3px solid white;\n"
                                       "padding : 4px ;\n"
                                       "}\n"
                                       "")
        self.greenbutton.setObjectName("greenbutton")
        self.horizontalLayout_2.addWidget(self.greenbutton)
        self.redbutton = QtWidgets.QPushButton(self.horizontalWidget)
        self.redbutton.setMinimumSize(QtCore.QSize(148, 0))
        self.redbutton.setStyleSheet("QPushButton{ \n"
                                     "background-color: #C33C54 ;\n"
                                     "border-radius: 5px;\n"
                                     "color : white ;\n"
                                     "border: none;\n"
                                     "font: 12pt \"Segoe UI\";\n"
                                     "padding-top : 7px ;\n"
                                     "padding-bottom : 7px ;\n"
                                     "padding-right : 27px ;\n"
                                     "padding-left : 27px ;\n"
                                     " }\n"
                                     "QPushButton:hover{\n"
                                     "border: 3px solid white;\n"
                                     "padding : 4px ;\n"
                                     "}\n"
                                     "")
        self.redbutton.setObjectName("redbutton")
        self.horizontalLayout_2.addWidget(self.redbutton)
        self.verticalLayout_2.addWidget(
            self.horizontalWidget, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.verticalWidget_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
    
        self.titeldialgue.setText("TextLabel")
        self.bodymessage.setText("just text")
        self.greenbutton.setText("YES")
        self.redbutton.setText( "NO")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
