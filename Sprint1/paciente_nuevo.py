# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paciente_nuevo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_paciente_nuevo(object):
    def setupUi(self, paciente_nuevo):
        paciente_nuevo.setObjectName("paciente_nuevo")
        paciente_nuevo.resize(677, 214)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        paciente_nuevo.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(paciente_nuevo)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 541, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(paciente_nuevo)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 19))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(paciente_nuevo)
        self.label_9.setGeometry(QtCore.QRect(610, 140, 51, 71))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/logo2.png"))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(paciente_nuevo)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 211, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(paciente_nuevo)
        self.pushButton.setGeometry(QtCore.QRect(410, 180, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(paciente_nuevo)
        self.label_3.setGeometry(QtCore.QRect(380, 60, 91, 19))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(paciente_nuevo)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 60, 201, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(paciente_nuevo)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(paciente_nuevo)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 150, 251, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(paciente_nuevo)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 81, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(paciente_nuevo)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 68, 19))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(paciente_nuevo)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 150, 201, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(paciente_nuevo)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 531, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(paciente_nuevo)
        self.label_7.setGeometry(QtCore.QRect(300, 150, 51, 19))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(paciente_nuevo)
        QtCore.QMetaObject.connectSlotsByName(paciente_nuevo)

    def retranslateUi(self, paciente_nuevo):
        _translate = QtCore.QCoreApplication.translate
        paciente_nuevo.setWindowTitle(_translate("paciente_nuevo", "Paciente nuevo"))
        self.label.setText(_translate("paciente_nuevo", "Paciente: "))
        self.label_4.setText(_translate("paciente_nuevo", "Fecha: 21/07/2021 13:25:48"))
        self.pushButton.setText(_translate("paciente_nuevo", "Agregar"))
        self.label_3.setText(_translate("paciente_nuevo", "dd/mm/aaaa"))
        self.label_2.setText(_translate("paciente_nuevo", "Fecha de nacimiento:"))
        self.label_5.setText(_translate("paciente_nuevo", "Dirección:"))
        self.label_6.setText(_translate("paciente_nuevo", "Teléfono:"))
        self.label_7.setText(_translate("paciente_nuevo", "e-mail:"))
