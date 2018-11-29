#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        """ Método que se ejecuta antes de cada prueba """
        self.pan = Item('pan', 12)
        self.jugo = Item('jugo', 5)

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self):
        """ Método que se ejecuta después da cada prueba """
        pass

    def test_cinco_mas_cinco_igual_diez(self):
        """ Test sencillo que siempre debe pasar """
        assert 5+5 == 10

    def test_nombre_producto_pan(self):
        """ Test para el nombre de producto """
        self.assertEqual(self.pan.name, 'pan')

    def test_nombre_producto_no_manzana(self):
        """ Test para nombre de producto """
        self.assertNotEqual(self.jugo.name, 'manzana')

    def test_contiene_productos(self):
        """ Test para productos en el carrito """
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos(self):
        """ Test de eliminar items del carrito """
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto_pan(self):
        """ Test para obtener un producto (pan) """
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)

    def test_excepcion_obtener_jugo(self):
        """ Test para verificar la excepcion lanzada 
         al obtener producto que no esté en el carrito 
        """
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto(self):
        """ Test para validar que el precio total sea el correcto """
        total = self.shopping_cart.total()

        self.assertGreater(total, 0)
        self.assertLess(total, self.pan.price +1)
        self.assertEqual(total, self.pan.price)

    def test_codigo_producto(self):
        """ Test para validar que el código del producto 
         contenga el nombre del producto
        """
        self.assertRegex(self.pan.code(), self.pan.name)
    
    def test_fail(self):
        """ Test para probar el método fail """
        if 2 > 3: # 3 > 2 para ejecutar el método
            self.fail('2 no es mayor a 3')

    # @unittest.skip("Motivos para saltar la prueba")
    # @unittest.skipUnless(False, "Motivos para saltar la prueba")
    @unittest.skipIf(True, "Motivos para saltar la prueba")
    def test_prueba_skip(self):
        """ Test que será omitido, decoramos para indicar que no será ejecutado """
        pass


if __name__ == '__main__':
    unittest.main()

""" 
Correr coverage para los test de covertura

coverage run test_shopping_cart.py
coverage report -m shopping_cart.py

Generar reportes en html
coverage html shopping_cart.py

cd htmlcov
python -m http.server
"""