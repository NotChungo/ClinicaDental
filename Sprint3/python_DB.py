import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_paciente(conn, datos):

    sql = ''' INSERT INTO paciente(nombre, direccion, telefono, email, nacimiento, documentos)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, datos)
    conn.commit()
    return cur.lastrowid

def find_paciente_por_nombre(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT * FROM paciente WHERE nombre LIKE ?", (codigo,))
    rows = cur.fetchall()
    return rows

def find_id_por_nombre(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT id FROM paciente WHERE nombre= ?", (codigo,))
    rows = cur.fetchall()
    return rows

def select_nombre_por_id(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT nombre  FROM paciente WHERE id=?", (codigo,))

    rows = cur.fetchall()
    return rows

def create_tratamiento(conn, datos):
    sql = ''' INSERT INTO tratamiento(paciente_id, fecha, tratamiento, descripcion, abono, total, resta)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, datos)
    conn.commit()
    return cur.lastrowid

def select_tratamiento_por_id(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT * FROM tratamiento WHERE paciente_id = ?", (codigo,))
    rows = cur.fetchall()
    return rows

def select_pago_por_id(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE id = ?", (codigo,))
    rows = cur.fetchall()
    return rows

def select_tratamiento_pornombre(conn, trat):

    cur = conn.cursor()
    cur.execute("SELECT * FROM tratamiento WHERE tratamiento = ?", (trat,))
    rows = cur.fetchall()
    return rows

def select_tratamiento_por_id_trat(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT * FROM tratamiento WHERE id = ?", (codigo,))
    rows = cur.fetchall()
    return rows

def actualizar_resta_por_id_trat(conn, codigo, resta):

    cur = conn.cursor()
    sql = "UPDATE tratamiento SET resta = "+ str(resta) + " WHERE id = " + str(codigo) + ";"
    cur.execute(sql)
    conn.commit()
    return

def create_caja(conn, datos):

    sql = ''' INSERT INTO caja(tratamiento_id, vales_pago, fecha, consultorio, descripcion, abono, cargo, banco, notas)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, datos)
    conn.commit()
    return cur.lastrowid

def last_element_caja(conn):

    sql = '''SELECT * FROM caja WHERE id=(SELECT max(id) FROM caja);'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def select_pago_por_trat_id(conn, codigo):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE tratamiento_id = ?", (codigo,))
    rows = cur.fetchall()
    return rows

def select_pago_por_fecha(conn, codigo, fecha):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE vales_pago = ? AND fecha = ?", (codigo, fecha))
    rows = cur.fetchall()
    return rows

def select_entrada_caja(conn, fecha):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE vales_pago = 0 AND fecha = ?", (fecha,))
    rows = cur.fetchall()
    return rows

def select_salida_caja(conn, fecha):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE vales_pago > 0 AND fecha = ?", (fecha,))
    rows = cur.fetchall()
    return rows

def select_pago_manolito_caja(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM caja WHERE descripcion = 'Manolo'")
    rows = cur.fetchall()
    return rows
