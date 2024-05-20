# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abono.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_abonos(object):
    def setupUi(self, abonos):
        abonos.setObjectName("abonos")
        abonos.resize(796, 537)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        abonos.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(abonos)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 541, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(abonos)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(abonos)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 101, 19))
        self.label_7.setObjectName("label_7")
        self.listWidget = QtWidgets.QListWidget(abonos)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 256, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(abonos)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 91, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(abonos)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 50, 191, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(abonos)
        self.label_3.setGeometry(QtCore.QRect(320, 90, 101, 19))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(abonos)
        self.label_9.setGeometry(QtCore.QRect(730, 460, 51, 71))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/logo2.png"))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(abonos)
        self.label_4.setGeometry(QtCore.QRect(430, 460, 211, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(abonos)
        self.pushButton.setGeometry(QtCore.QRect(610, 500, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(abonos)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 91, 17))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(abonos)
        self.label_8.setGeometry(QtCore.QRect(0, 460, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(abonos)
        self.label_10.setGeometry(QtCore.QRect(0, 500, 91, 17))
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(abonos)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 500, 86, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(['1', '2'])
        self.comboBox_2 = QtWidgets.QComboBox(abonos)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 460, 161, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(['Efectivo', 'Transferencia'])
        self.label_6 = QtWidgets.QLabel(abonos)
        self.label_6.setGeometry(QtCore.QRect(320, 120, 141, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(abonos)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 90, 191, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textBrowser = QtWidgets.QTextBrowser(abonos)
        self.textBrowser.setGeometry(QtCore.QRect(105, 211, 671, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(abonos)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 140, 461, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(abonos)
        QtCore.QMetaObject.connectSlotsByName(abonos)

    def retranslateUi(self, abonos):
        _translate = QtCore.QCoreApplication.translate
        abonos.setWindowTitle(_translate("abonos", "Abonos"))
        self.label.setText(_translate("abonos", "Paciente: "))
        self.label_7.setText(_translate("abonos", "Tratamientos:"))
        self.label_2.setText(_translate("abonos", "Abono:"))
        self.label_3.setText(_translate("abonos", "Tratamiento:"))
        self.label_4.setText(_translate("abonos", ""))
        self.pushButton.setText(_translate("abonos", "Agregar"))
        self.label_5.setText(_translate("abonos", "Descripcion:"))
        self.label_8.setText(_translate("abonos", "Pago en:"))
        self.label_10.setText(_translate("abonos", "Consultorio:"))
        self.label_6.setText(_translate("abonos", "Trabajo realizado:"))
