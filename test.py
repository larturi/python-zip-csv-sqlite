import unittest
from coches import *

nombre_fichero = 'test.csv'

class test_count_coches(unittest.TestCase):
    def test_count_coches(self):
        
        borrar_bd()
        datos = leer_datos(nombre_fichero)
        conexion = crear_conexion_bd()
        crear_tabla_coches(conexion)
        grabar_coche(conexion, datos)
        
        count = count_coches(conexion)

        self.assertEqual(count, 2780)
        
        
if __name__ == '__main__':
    unittest.main()
    