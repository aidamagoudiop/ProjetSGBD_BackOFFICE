# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(428, 0)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, -50, 480, 571))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background:rgba(45, 100, 135, 0.533);\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 110, 251, 31))
        self.plainTextEdit.setStyleSheet("color: whitesmoke;\n"
"text-transform: uppercase;\n"
"background-color: transparent;\n"
"text-align: center;\n"
"justify-content:center;\n"
"font-size:2em;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 341, 101))
        self.tableWidget.setStyleSheet("border: 2px solid whitesmoke;\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 290, 341, 111))
        self.tableWidget_2.setStyleSheet("border: 2px solid whitesmoke;")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 180, 291, 31))
        self.label.setStyleSheet("background-color: transparent;\n"
"color: whitesmoke;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 330, 291, 31))
        self.label_2.setStyleSheet("background-color: transparent;\n"
"color: whitesmoke;\n"
"text-transform: uppercase;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit.setPlainText(_translate("Form", "Bienvenu(e)! Que souhaitez-vous faire ?"))
        self.label.setText(_translate("Form", "GESTION DE L’EFFECTIVITE DES ENSEIGNEMENTS "))
        self.label_2.setText(_translate("Form", "Suivi périodique des enseignements effectués "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())