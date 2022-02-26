from os import remove
import sqlite3
import sys
from zipfile import ZipFile
import pandas as pd
import sqlite3
from sqlite3 import Error

basededatos = 'coches.db'

def print_hr():
    print('-' * 80)

def descomprimir_fichero(nombre):
    with ZipFile(nombre, 'r') as zip:
        zip.extractall()
        print(' ✓ Fichero zip descomprimido')
        
def borrar_bd():
    try:
        remove(basededatos)
    except FileNotFoundError:
        pass
    print(' ✓ BD vieja eliminada')

def leer_datos(nombre):
    datos = pd.read_csv(nombre, sep=';')
    return datos

def crear_conexion_bd():
    try:
        conexion = sqlite3.connect(basededatos)
        print(' ✓ Conexion establecida')
        return conexion
    except Error:
        print(Error)
        
def crear_tabla_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE coches(marca text, modelo text, combustible text, transmision text, estado text, matricula text, kilometraje integer, potencia real, precio real)')
    conexion.commit()
    print(' ✓ Tabla coches creada')
    
def insertar_tabla_coches(conexion, coche):
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO coches VALUES(?,?,?,?,?,?,?,?,?)', coche)
    conexion.commit()
    
def grabar_coche(conexion, datos):
    for fila in datos.itertuples():
        marca = fila[1]
        modelo = fila[2]
        combustible = fila[3]
        transmision = fila[4]
        estado = fila[5]
        matricula = fila[6]
        kilometraje = fila[7]
        potencia = fila[8]
        precio = fila[9]
        
        coche = (marca, modelo, combustible, transmision, estado, matricula, kilometraje, potencia, precio)
        
        insertar_tabla_coches(conexion, coche)
        
    print(' ✓ Datos insertados')

def consultar_coches(conexion):
    print('\nConsultamos los 10 primeros coches de {}'.format(str(count_coches(conexion))))
    print_hr()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM coches LIMIT 10')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def count_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM coches')
    count = cursor.fetchall()
    return count[0][0]
    
def procesar_datos():
    nombre_fichero = sys.argv[1]
    
    borrar_bd()

    descomprimir_fichero(nombre_fichero)
    datos = leer_datos(nombre_fichero)
    
    conexion = crear_conexion_bd()
    crear_tabla_coches(conexion)
    
    grabar_coche(conexion, datos)
    
    # Consultas
    count_coches(conexion)
    consultar_coches(conexion)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print(
            "Error: Numero de parametros incorrecto. Debe ingresar el nombre del archivo.")
    else:
        procesar_datos()
