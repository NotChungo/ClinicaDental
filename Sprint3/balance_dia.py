# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balance_dia.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_balance_dia(object):
    def setupUi(self, balance_dia):
        balance_dia.setObjectName("balance_dia")
        balance_dia.resize(724, 393)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        balance_dia.setWindowIcon(icon)
        self.label_9 = QtWidgets.QLabel(balance_dia)
        self.label_9.setGeometry(QtCore.QRect(660, 320, 51, 71))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/logo2.png"))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(balance_dia)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 211, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(balance_dia)
        self.pushButton.setGeometry(QtCore.QRect(610, 10, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(balance_dia)
        self.label.setGeometry(QtCore.QRect(270, 10, 171, 19))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(balance_dia)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 611, 321))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(balance_dia)
        QtCore.QMetaObject.connectSlotsByName(balance_dia)

    def retranslateUi(self, balance_dia):
        _translate = QtCore.QCoreApplication.translate
        balance_dia.setWindowTitle(_translate("balance_dia", "Balance del día"))
        self.label_4.setText(_translate("balance_dia", "Fecha: 21/07/2021 13:25:48"))
        self.pushButton.setText(_translate("balance_dia", "Imprimir"))
        self.label.setText(_translate("balance_dia", "Registrados en el día:"))
