# coding: utf-8

import unittest

from celular import letra


class TestSum(unittest.TestCase):
    def test_tecla_a(self):
        self.assertEqual(letra('a'),'2')

    def test_tecla_b(self):
        self.assertEqual(letra('b'),'22')
        
    def test_tecla_c(self):
        self.assertEqual(letra('c'),'222')
    
    def test_tecla_d(self):
        self.assertEqual(letra('d'),'3')
    
    def test_tecla_e(self):
        self.assertEqual(letra('e'),'33')

    def test_tecla_f(self):
        self.assertEqual(letra('f'),'333')

    def test_tecla_z(self):
        self.assertEqual(letra('z'),'9999')

    def test_tecla_(self):
        self.assertEqual(letra('z'),'9999')


if __name__ == '__main__':
    unittest.main()
