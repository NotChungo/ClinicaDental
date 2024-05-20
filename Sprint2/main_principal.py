import sys
import os
import webbrowser
import python_DB
from datetime import datetime, timedelta
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from abono import*
from paciente_nuevo import*
from balance_dia import*
from pago_inicial import*
from principal import*
from funciones_extra import *



database = "pacientes.db"
path_dir = ""
paciente_encontrado = ''
id_paciente = ''

class Ui_paciente_nuevo(QtWidgets.QMainWindow,Ui_paciente_nuevo):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)


        self.setupUi(self)
        self.pushButton.clicked.connect(self.agregar_paciente)
        fecha = datetime.now()
        dt_string = fecha.strftime("%d/%m/%Y %H:%M:%S")
        self.label_4.setText('')
        self.label_4.setText("Fecha: "+ str(dt_string))

    def agregar_paciente(self):
        nombre = self.lineEdit.text()
        direccion = self.lineEdit_3.text()
        telefono = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        nacimiento = self.lineEdit_2.text()
        documentos = self.lineEdit.text()
        datos = (nombre, direccion, telefono, email, nacimiento,
        documentos)
        conn = python_DB.create_connection(database)
        python_DB.create_paciente(conn,datos)
        self.close()


class Ui_abonos(QtWidgets.QMainWindow,Ui_abonos):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.tratamiento_id = ''
        fecha = datetime.now()
        dt_string = fecha.strftime("%d/%m/%Y %H:%M:%S")
        self.label_4.setText("Fecha: "+ str(dt_string))
        global paciente_encontrado, id_paciente
        self.setupUi(self)
        if paciente_encontrado == '':
            self.lineEdit.setText("No se ha definido un paciente en la pantalla principal")
        self.pushButton.clicked.connect(self.agregar_abono)
        if paciente_encontrado !='':
            conn = python_DB.create_connection(database)
            nombre_paciente = python_DB.select_nombre_por_id(conn, str(paciente_encontrado))
            nombre_paciente = str(nombre_paciente)
            self.lineEdit.setText(nombre_paciente[3:-4])
            coincidencias = busqueda_tratamientos(conn, id_paciente)
            if len(coincidencias) == 0:
                coincidencias.append("El paciente no tiene tratamientos")
            if len(coincidencias) > 0:
                self.listWidget.clear()
                for i in coincidencias:
                    pos = 0
                    self.listWidget.insertItem(pos,i)
                    pos += 1
            cursor = self.listWidget.itemClicked.connect(self.seleccionado)

    def seleccionado(self):
        selec = self.listWidget.currentItem().text()
        selec = selec.split(' ')
        tratamiento = selec[0]
        conn = python_DB.create_connection(database)
        elementos = python_DB.select_tratamiento_por_id_trat(conn,tratamiento)
        elementos = str(elementos)
        elementos = elementos.split(',')
        parrafo = elementos[4]
        parrafo = parrafo[2:-1]
        parrafo = parrafo.split(r'\n')
        texto_a1 = ''
        for i in parrafo:
            texto_a1 = texto_a1 + i + '\n'
        self.lineEdit_4.setText(elementos[3])
        total = '<span style=\" color: #0000AA;">Total </span>'
        resta = '<span style=\" color: #0000AA;">Resta </span>'
        cadena = elementos[3] + 'fecha inicio de tratamiento:' + elementos[2] + '\n' + texto_a1 #+ total + elementos[6] + resta + elementos[7]
        self.textBrowser.setText(cadena)
        self.textBrowser.append('<span style=\" color: #0000AA;">Total %s</span>'%elementos[6])
        restan = elementos[7]
        restan = restan [:-2]
        self.textBrowser.append('<span style=\" color: #0000AA;">Resta %s</span>'%restan)
        self.tratamiento_id = elementos[0]
        self.tratamiento_id = self.tratamiento_id[2:]
        pagos_recientes = python_DB.select_pago_por_trat_id(conn, self.tratamiento_id)
        #pagos_recientes  = str(pagos_recientes).split(',')
        for i in pagos_recientes:
            elementos = i
            elementos = str(elementos).split(',')
            self.textBrowser.append(elementos[3] + " $" + elementos[6] + "\n")
            parrafo = elementos[5]
            parrafo = parrafo.split(r'\n')
            texto_a1 = ''
            for i in parrafo:
                texto_a1 = texto_a1 + i + '\n'
            self.textBrowser.append(texto_a1)

    def agregar_abono(self):
        global paciente_encontrado
        fecha = datetime.now()
        conn = python_DB.create_connection(database)
        coincidencias = 0
        if self.tratamiento_id == '':
            self.lineEdit_2.setText("No se ha seleccionado un tratamiento")
        if self.tratamiento_id != '':
            datos_pagos = python_DB.select_tratamiento_por_id_trat(conn,self.tratamiento_id)
            datos_pagos = str(datos_pagos)
            datos_pagos = datos_pagos.split(',')
            resta = datos_pagos[7]
            resta = resta[:-2]
            total = datos_pagos[6]
            abono = int(self.lineEdit_2.text())
            resta = int(resta) - abono
            python_DB.actualizar_resta_por_id_trat(conn, self.tratamiento_id, resta)
            fecha = datetime.now()
            fecha = fecha.strftime("%d/%m/%Y")
            pago = self.comboBox_2.currentText()
            if (pago == "Transferencia"): pago_e = 1
            if (pago != "Transferencia"): pago_e = 2
            tratamiento = self.lineEdit_4.text()
            tratamiento = tratamiento[2:-1]
            elemntos_ticket(self.lineEdit.text(), str(abono), str(resta), tratamiento)
            imprimir_ticket()
            consultorio = self.comboBox_3.currentText()
            descripcion = self.plainTextEdit.toPlainText()
            datos_caja = (self.tratamiento_id, 0, fecha, int(consultorio), descripcion, abono, 0, pago_e, '-')
            caja_escr = python_DB.create_caja(conn,datos_caja)
            self.close()




class Ui_pago_inicial(QtWidgets.QMainWindow,Ui_pago_inicial):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        global paciente_encontrado, id_paciente
        self.setupUi(self)
        fecha = datetime.now()
        dt_string = fecha.strftime("%d/%m/%Y %H:%M:%S")
        self.label_4.setText('')
        self.label_4.setText("Fecha: "+ str(dt_string))
        if paciente_encontrado == '':
            self.lineEdit.setText("No se ha definido un paciente en la pantalla principal")
        self.pushButton.clicked.connect(self.agregar_tratamiento)
        if paciente_encontrado !='':
            conn = python_DB.create_connection(database)
            nombre_paciente = python_DB.select_nombre_por_id(conn, str(paciente_encontrado))
            nombre_paciente = str(nombre_paciente)
            self.lineEdit.setText(nombre_paciente[3:-4])

            tratamientos_paciente = python_DB.select_tratamiento_por_id(conn, id_paciente)
            coincidencias = []
            for datos in tratamientos_paciente:
                captura = str(datos)
                captura = captura.split(',')
                nombre_tratamiento = captura[3]
                nombre_tratamiento = nombre_tratamiento[2:-2]
                id_tratamiento = captura[0]
                id_tratamiento = id_tratamiento[1:]
                coincidencias.append(nombre_tratamiento)
            if len(coincidencias) == 0:
                coincidencias.append("El paciente no tiene tratamientos")
            if len(coincidencias) > 0:
                for i in coincidencias:
                    pos = 0
                    self.listWidget.insertItem(pos,i)
                    pos += 1



    def agregar_tratamiento(self):
        global paciente_encontrado
        conn = python_DB.create_connection(database)
        paciente_id = paciente_encontrado
        tratamiento = self.comboBox.currentText()
        abono = int(self.lineEdit_2.text())
        total = int(self.lineEdit_4.text())
        resta = total - abono
        descripcion = self.plainTextEdit.toPlainText()
        fecha = datetime.now()
        fecha = fecha.strftime("%d/%m/%Y")
        datos = (paciente_id, fecha, tratamiento,descripcion, abono, total, resta)
        tratamiento_id = python_DB.create_tratamiento(conn,datos)
        fecha_imp = datetime.now()
        dt_string = fecha_imp.strftime("%d/%m/%Y %H:%M:%S")
        self.label_4.setText("Fecha: "+ str(dt_string))
        pago = self.comboBox_2.currentText()
        if (pago == "Transferencia"): pago_e = 1
        if (pago != "Transferencia"): pago_e = 2
        elemntos_ticket(self.lineEdit.text(), str(abono), str(resta), tratamiento)
        imprimir_ticket()
        consultorio = self.comboBox_3.currentText()
        trat_id = python_DB.last_element_caja(conn)
        datos_caja = (trat_id, 0, fecha, int(consultorio), descripcion, abono, 0, pago_e, '-')
        caja_escr = python_DB.create_caja(conn,datos_caja)
        self.close()



class Ui_balance_dia(QtWidgets.QMainWindow,Ui_balance_dia):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)

        self.setupUi(self)
        fecha = datetime.now()
        conn = python_DB.create_connection(database)
        fecha = fecha.strftime("%d/%m/%Y")
        archivo = open('reporte.html','w')
        texto = '''<html>
        <style>
        table, th, td {
        border:1px solid black;
        }
        </style>
        <body>\n'''
        archivo.write(texto)
        datos_entradas = python_DB.select_entrada_caja(conn,fecha)
        #print(datos_entradas)
        a_c1 = 0
        a_c2 = 0
        c_c1 = 0
        c_c2 = 0
        a_efec = 0
        a_trans = 0
        c_efec = 0
        c_trans = 0
        pe = 0 #Pasajes Emily
        ps = 0 #Psicologo
        ti = 0 #Tita
        ga = 0 #Gasolina
        ca = 0 #Comida
        pa = 0 #Pago Almen
        ot = 0 #Otros
        ma = 0 #Material
        tr = 0 #Trab. laboratorio
        co = 0 #Colegiaturas
        mn = 0 #Manolo
        mj = 0 #Manejo de cuenta
        p_cir = 0 #Pago Cirujano
        p_end = 0 #Pago Endodoncista
        p_per = 0 #Pago Periodoncista
        texto = '<h2>Reporte del día ' + fecha + '</h2>\n'
        archivo.write(texto)
        texto = '''
        <table style="width:70%">
        <tr>
        <th>Descripción/Nombre Paciente</th>
        <th>Abono</th>
        <th>Cargo</th>
        </tr>
        '''
        archivo.write(texto)

        for i in datos_entradas:
            cadena = i
            cadena = str(cadena).split(',')
            consul = int(cadena[4])
            modo_pago = cadena[8]
            modo_pago = int(modo_pago)
            trat_id = cadena[1]
            paciente = python_DB.select_tratamiento_por_id_trat(conn, trat_id)
            paciente = paciente[0]
            paciente = paciente[1]
            nombre_paciente = python_DB.select_nombre_por_id(conn, paciente)
            nombre_paciente = str(nombre_paciente)
            nombre_paciente = nombre_paciente[3:-4]
            if (consul == 1): a_c1 = a_c1 + int(cadena[6])
            if (consul == 2): a_c2 = a_c2 + int(cadena[6])
            if (modo_pago == 1):
                a_trans = a_trans + int(cadena[6])
                print(a_c1)
                texto = ('<tr> <td><i>' + nombre_paciente + ' (trans. banco) </i></td>\n'
                + '<td>' + str(cadena[6]) + '</td>\n' +'<td> </td></tr>\n' )
            if (modo_pago == 2):
                a_efec = a_efec + int(cadena[6])
                print(a_c2)
                texto = ('<tr> <td>' + nombre_paciente + '</td>\n'
                + '<td>' + str(cadena[6]) + '</td>\n' +'<td> </td></tr>\n' )
            archivo.write(texto)

        self.textBrowser.append('Ingresos consultorio <span style="color:#0000ff;"><b>%s <\b>\n</span>' %str(a_c1))
        self.textBrowser.append('********************************************************')
        self.textBrowser.append('********************************************************')
        self.textBrowser.append('Ingresos en efectivo <span style="color:#0000ff;"><b>%s <\b>\n</span>' %str(a_efec))
        self.textBrowser.append('Ingresos por transferencia <span style="color:#0000ff;"><b>%s <\b>\n</span>' %str(a_trans))
        self.textBrowser.append('********************************************************')
        self.textBrowser.append('********************************************************')
        datos_pagos = python_DB.select_salida_caja(conn,fecha)
        for i in datos_pagos:
            cadena = i
            if (cadena[5] != 'Endodoncista' and cadena[5] != 'Cirujano' and cadena[5] != 'Periodoncista'):
                c_c1 = c_c1 + int(cadena[7])
            if (cadena[5] == 'Endodoncista' or cadena[5] == 'Cirujano' or cadena[5] == 'Periodoncista'):
                c_c2 = c_c2 + int(cadena[7])
            modo_pago = cadena[8]
            if (modo_pago == '1'): c_trans = c_trans + int(cadena[7])
            if (modo_pago == '2'): c_efec = c_efec + int(cadena[7])
            #*******************
            #*******************
            # elementos para la grafica
            #con gastos desglosados
            #*******************
            #*******************

        texto = ('<tr> <td><b>Total </b></td>\n'
                + '<td>' + str(a_c1 + a_c2) + '</td>\n' +'<td> ' + str(c_c1 + c_c2) +'</td></tr>\n' )
        archivo.write(texto)
        archivo.write('</table>')
        ganancia = (a_c1 + a_c2) - (c_c1 + c_c2)
        texto = '<h3>Ganancia del día ' + str(ganancia) + '</h3>\n'
        archivo.write(texto)
        archivo.write('</body></html>')

        archivo.close()
        if c_c1 !=0:
            fig, (ax0,ax1) = plt.subplots(2, figsize=(12,8), height_ratios=[1, 2])

            fruits = ['Ingresos', 'Egresos']
            counts = [a_c1, c_c1]
            bar_labels = ['Ingresos', 'Egresos']
            bar_colors = ['tab:red', 'tab:blue']

            ax0.bar(fruits, counts, label=bar_labels, color=bar_colors)

            ax0.set_ylabel('Cantidad')
            ax0.set_title('Consultorio 1')
            ax0.legend(title='E/G')
            labels = ['Pasajes Emily' , 'Psicologo', 'Tita', 'Gasolina', 'Comida', 'Pago Almen',
            'Material', 'Trab. laboratorio', 'Colegiaturas', 'Manolo', 'Manejo de cuenta', 'Otros']
            sizes = [100*(pe/c_c1), 100*(ps/c_c1), 100*(ti/c_c1), 100*(ga/c_c1), 100*(ca/c_c1),
            100*(pa/c_c1),100*(ma/c_c1), 100*(tr/c_c1), 100*(co/c_c1), 100*( mn/c_c1), 100*(mj/c_c1),
            100*(ot/c_c1)]
            bar_labels = ['Pasajes Emily' , 'Psicologo', 'Tita', 'Gasolina', 'Comida', 'Pago Almen',
            'Material', 'Trab. laboratorio', 'Colegiaturas', 'Manolo', 'Manejo de cuenta', 'Otros']
            bar_colors = ['orange', 'chocolate', 'orange', 'chocolate', 'orange', 'chocolate',
            'orange', 'chocolate', 'orange', 'chocolate', 'orange', 'chocolate']
            datos_plot = pd.Series(sizes)

            ax1 = datos_plot.plot(kind='bar')
            ax1.set_ylabel('Distribucion de egreso %')
            ax1.set_xticklabels(bar_labels)
            plt.subplots_adjust(bottom=0.25)
            plt.show()


        if c_c2 != 0 :
            fig1, (ax2,ax3) = plt.subplots(2, figsize=(12,8), height_ratios=[1, 2])
            fruits = ['Ingresos', 'Egresos']
            counts = [a_c2, c_c2]
            bar_labels = ['Ingresos', 'Especialista']
            bar_colors = ['tab:red', 'tab:blue']

            ax2.bar(fruits, counts, label=bar_labels, color=bar_colors)

            ax2.set_ylabel('Cantidad')
            ax2.set_title('Consultorio 2')
            ax2.legend(title='E/G')

            labels = ['Endodoncista' , 'Cirujano' , 'Periodoncista' ]
            sizes = [100*(p_end/c_c2), 100*(p_cir/c_c2), 100*(p_per/c_c2)]
            bar_labels = ['Endodoncista' , 'Cirujano' , 'Periodoncista' ]
            datos_plot = pd.Series(sizes)
            ax3 = datos_plot.plot(kind='bar')
            ax3.set_ylabel('Distribucion de egreso %')
            ax3.set_xticklabels(bar_labels)
            plt.subplots_adjust(bottom=0.25)
            plt.show()

        self.pushButton.clicked.connect(self.mostrar_reporte)

    def agregar_fila_reporte (self, modo_pago, nombre, cargo):
        if (modo_pago == 1):
            texto = ('<tr> <td><i>' + nombre + ' (trans. banco) </i></td>\n'
             +'<td> </td>\n' + '<td>' + str(cargo) + '</td></tr>\n')
        if (modo_pago == 2):
            texto = ('<tr> <td>' + nombre + '</td>\n'
            +'<td> </td>\n' + '<td>' + str(cargo) + '</td></tr>\n')

        return(texto)

    def mostrar_reporte(self):
        url = "reporte.html"
        webbrowser.open(url,new = 2)


class Ui_Concultorio(QtWidgets.QMainWindow,Ui_Concultorio):


    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionAgregar_paciente.triggered.connect(self.config_paciente)
        self.actionAbono.triggered.connect(self.config_abono)
        self.actionPago_inicial_tratamientos.triggered.connect(self.config_pago_inicial)
        self.actionBalance_del_d_a.triggered.connect(self.config_balancedia)

        self.pushButton.clicked.connect(self.encontrar_elementos)

    def encontrar_elementos(self):
        self.conn = python_DB.create_connection(database)
        global paciente_encontrado, id_paciente
        if self.lineEdit.text() != '':

            nombre = self.lineEdit.text()
            nombre = "%"+nombre +"%"
            datos = python_DB.find_paciente_por_nombre(self.conn, nombre)
            coincidencias = 0
            if len(str(datos)) > 3:


                for dato in datos:
                        coincidencias = coincidencias + 1

                if coincidencias > 1:
                        self.textBrowser.clear()
                        self.lineEdit.clear()
                        self.lineEdit_2.clear()
                        self.lineEdit_3.clear()
                        self.lineEdit_4.clear()
                        self.lineEdit_5.clear()
                        self.textBrowser.append('<span style="color:#0000ff;">Se encontraron los siguientes pacientes:\n </span>')
                        for dato in datos:
                            dato = str(dato)
                            captura = dato.split(',')
                            #id_vinculo = captura[1]
                            self.textBrowser.append('<span style="color:#0000ff;"><b>%s <\b>\n</span>'%captura[1])
                        self.textBrowser.append('<span style="color:#0000ff;">Escriba el nombre del paciente\n </span>')
                        self.textBrowser.append('<span style="color:#0000ff;">para mostrar la informacion almacenada\n </span>')


                if coincidencias == 1:
                    self.textBrowser.clear()
                    datos = str(datos)
                    captura = datos.split(',')
                    paciente_encontrado = captura[0]

                    paciente_encontrado = paciente_encontrado[2:]
                    id_paciente = paciente_encontrado

                    self.lineEdit.setText(captura[1])
                    self.lineEdit_2.setText(captura[5])
                    self.lineEdit_3.setText(captura[2])
                    self.lineEdit_4.setText(captura[3])
                    self.lineEdit_5.setText(captura[4])
                conn = python_DB.create_connection(database)
                coincidencias = busqueda_tratamientos(conn, id_paciente)
                if len(coincidencias) == 0:
                    coincidencias.append("El paciente no tiene tratamientos")
                if len(coincidencias) > 0:
                    self.listWidget.clear()
                    for i in coincidencias:
                        pos = 0
                        self.listWidget.insertItem(pos,i)
                        pos += 1
                cursor = self.listWidget.itemClicked.connect(self.seleccionado_1)
            if len(str(datos)) <= 3:
                self.textBrowser.append('<span style="color:#ff0000;">Paciente no se encuentra en base de datos </span>')
    def seleccionado_1(self):
        selec = self.listWidget.currentItem().text()
        selec = selec.split(' ')
        tratamiento = selec[0]
        conn = python_DB.create_connection(database)
        elementos = python_DB.select_tratamiento_por_id_trat(conn,tratamiento)
        elementos = str(elementos)
        elementos = elementos.split(',')
        parrafo = elementos[4]
        parrafo = parrafo[2:-1]
        parrafo = parrafo.split(r'\n')
        texto_a1 = ''
        for i in parrafo:
            texto_a1 = texto_a1 + i + '\n'
        total = '<span style=\" color: #0000AA;">Total </span>'
        resta = '<span style=\" color: #0000AA;">Resta </span>'
        cadena = elementos[3] + '  fecha inicio de tratamiento:' + elementos[2] + '\n'#+ total + elementos[6] + resta + elementos[7]
        self.textBrowser.setText('<i> %s <\i>'%cadena)
        self.textBrowser.append('<i><b> Nota de inicio de tratamiento<\i><\b>')
        self.textBrowser.append(texto_a1)
        self.textBrowser.append('<span style=\" color: #0000AA;">Total %s</span>'%elementos[6])
        restan = elementos[7]
        restan = restan [:-2]
        self.textBrowser.append('<span style=\" color: #0000AA;">Resta %s</span>'%restan)
        self.tratamiento_id = elementos[0]
        self.tratamiento_id = self.tratamiento_id[2:]
        pagos_recientes = python_DB.select_pago_por_trat_id(conn, self.tratamiento_id)
        #pagos_recientes  = str(pagos_recientes).split(',')
        for i in pagos_recientes:
            elementos = i
            elementos = str(elementos).split(',')
            self.textBrowser.append(elementos[3] + " $" + elementos[6] + "\n")
            parrafo = elementos[5]
            parrafo = parrafo.split(r'\n')
            texto_a1 = ''
            for i in parrafo:
                texto_a1 = texto_a1 + i + '\n'
            self.textBrowser.append(texto_a1)

    def config_paciente(self):

        self._paciente = Ui_paciente_nuevo()
        self._paciente.show()

    def config_abono(self):

        self._abono = Ui_abonos()
        self._abono.show()

    def config_pago_inicial(self):

        self._pago_inicial = Ui_pago_inicial()
        self._pago_inicial.show()

    def config_balancedia(self):

        self._config_balancedia = Ui_balance_dia()
        self._config_balancedia.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Concultorio()
    window.show()
    app.exec_()
