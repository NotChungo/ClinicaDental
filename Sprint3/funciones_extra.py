import python_DB
import os
from datetime import datetime, timedelta

database = "pacientes.db"

def imprimir_ticket():
    #Busca los nombres de las impresoras_____lpstat -p -d
    comando = 'lpr -P SUPERRISC_S31 ticket.txt '
    os.system(comando)
    return

def elemntos_ticket(nombre, abono, resta, tratamiento):
    archivo = open('ticket.txt','w')
    header = '__________________\n'
    header = header + 'Estomatologa\n'
    header = header + 'Liliana Serrano F\n'
    header = header + 'Ced. 6231337\n'
    header = header + 'Tel: 244 102 3383\n'
    header = header + '__________________\n'
    archivo.write(header)
    texto = 'Paciente: ' + nombre + '\n'
    texto = texto + 'Trat.: ' + tratamiento + '\n'
    texto = texto + 'Abono: ' + abono + '\n'
    texto = texto + 'Resta: ' + resta + '\n'
    texto = texto + '__________________' + '\n'
    fecha = datetime.today().strftime("%d %b, %Y")
    texto = texto + fecha
    archivo.write(texto)

    return

def busqueda_tratamientos(conn,id_paciente):
    conn = python_DB.create_connection(database)
    tratamientos_paciente = python_DB.select_tratamiento_por_id(conn, id_paciente)
    coincidencias = []
    for datos in tratamientos_paciente:
                    captura = str(datos)
                    captura = captura.split(',')
                    nombre_tratamiento = captura[3]
                    nombre_tratamiento = nombre_tratamiento[2:-1]
                    fecha_x = captura[2]
                    id_tratamiento = captura[0]
                    id_tratamiento = id_tratamiento[1:]
                    nombre_tratamiento = id_tratamiento + ' ' + nombre_tratamiento + ' ' + fecha_x
                    coincidencias.append(nombre_tratamiento)
    return coincidencias
