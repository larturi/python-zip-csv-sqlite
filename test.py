import unittest
from coches import *

nombre_fichero = 'test.csv'
datos = leer_datos(nombre_fichero)

def set_environment():
    borrar_bd()
    conexion = crear_conexion_bd()
    crear_tabla_coches(conexion)
    grabar_coche(conexion, datos)
    return conexion

class test_count_coches(unittest.TestCase):
    def test_count_coches(self):
                
        conexion = set_environment()
       
        count = count_coches(conexion)
        self.assertEqual(count, 2780)
        
class test_precio_total_coches(unittest.TestCase):
    def test_precio_total_coches(self):
        
        conexion = set_environment()
        
        suma = suma_importe_coches(conexion)
        self.assertEqual(suma, 38997136.0)
        
        
if __name__ == '__main__':
    unittest.main()
    