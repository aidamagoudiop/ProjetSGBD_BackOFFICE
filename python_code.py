# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardCVpbWw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

from qframe1 import Qframe1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(556, 374)
        MainWindow.setStyleSheet(u"\n"
"\n"
"*{\n"
"border:none;\n"
"background-color: black;\n"
"}\n"
"\n"
"#side_menu{\n"
"border-radius:20px;\n"
"background-color:  #071e26;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:20px;\n"
"border-radius:5px;\n"
"background-color: #265e72;\n"
"}\n"
"\n"
"#main-body{\n"
"border-radius:105px;\n"
"background-color:  #071e26;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QSize(80, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(20, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn.setStyleSheet(u"color: whitesmoke;")

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 181, 32))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: whitesmoke;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(206, 0, 41, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_3.setStyleSheet(u"color: whitesmoke;\n"
"background-color:#265e72;\n"
"border: 1px solid #265e72;\n"
"border-radius: 100px;\n"
"")

        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.HorizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.HorizontalLayout_2.setSpacing(0)
        self.HorizontalLayout_2.setObjectName(u"HorizontalLayout_2")
        self.HorizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = Qframe1(self.frame_2)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(80, 0))
        self.leftMenu.setStyleSheet(u"background-color: #265e72;\n"
"border-radius: 10px;")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.leftMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(150, 0))
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_5)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(0, 50))
        self.homeBtn.setMaximumSize(QSize(501, 60))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.homeBtn.setFont(font2)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setLayoutDirection(Qt.RightToLeft)
        self.homeBtn.setStyleSheet(u"color: whitesmoke;\n"
"background-color: black;\n"
"border: 1px solid #265e72;\n"
"\n"
"border-left:4px solid #cc5bce;\n"
"background-color:#1b1b27; \n"
"font-weight:bold;")
        icon = QIcon()
        iconThemeName = u"home"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.homeBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.pvBtn = QPushButton(self.frame_5)
        self.pvBtn.setObjectName(u"pvBtn")
        font3 = QFont()
        font3.setPointSize(10)
        self.pvBtn.setFont(font3)
        self.pvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pvBtn.setLayoutDirection(Qt.RightToLeft)
        self.pvBtn.setStyleSheet(u"color: whitesmoke;\n"
"background-color: black;\n"
"border: 1px solid #265e72;")

        self.verticalLayout_3.addWidget(self.pvBtn)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.HorizontalLayout_2.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setStyleSheet(u"background-color: #1b1b27;\n"
"border-radius: 10px;")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.main_body)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 90, 71, 31))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:whitesmoke;")

        self.HorizontalLayout_2.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"\ue700  MENU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ADMINISTRATION", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ue77b", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"\ue80f   Home", None))
        self.pvBtn.setText(QCoreApplication.translate("MainWindow", u"\uee93  PV Sceance", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Corps", None))
    # retranslateUi

