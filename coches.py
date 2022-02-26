import sqlite3
import sys
from zipfile import ZipFile
import pandas as pd
import sqlite3
from sqlite3 import Error

basededatos = 'coches.db'

def descomprimir_fichero(nombre):
    with ZipFile(nombre, 'r') as zip:
        zip.extractall()


def leer_datos(nombre):
    datos = pd.read_csv(nombre, sep=';')
    return datos


def crear_conexion_bd():
    try:
        conexion = sqlite3.connect(basededatos)
        return conexion
    except Error:
        print(Error)
        
def crear_tabla_coches(conexion):
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE coches(marca text, modelo text, combustible text, transmision text, estado text, matricula text, kilometraje integer, potencia real, precio real)')
    conexion.commit()
    
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


def procesar_datos():
    nombre_fichero = sys.argv[1]

    descomprimir_fichero(nombre_fichero)
    datos = leer_datos(nombre_fichero)

    conexion = crear_conexion_bd()
    crear_tabla_coches(conexion)
    
    grabar_coche(conexion, datos)

    print(datos)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print(
            "Error: Numero de parametros incorrecto. Debe ingresar el nombre del archivo.")
    else:
        procesar_datos()
