import unittest
import sys
import os
from unittest.mock import patch
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Ruleta

# El código original que me diste
# Aquí estaría tu código de la ruleta sin cambios...

class TestRuleta(unittest.TestCase):

    def test_girar_ruleta(self):
        """Test para verificar que la función girar_ruleta() devuelve un número y un color válidos."""
        # Ejecutamos la función girar_ruleta y verificamos que el número y el color estén en la ruleta
        numero, color = Ruleta.girar_ruleta()
        self.assertIn(numero, Ruleta.ruleta)
        self.assertEqual(Ruleta.ruleta[numero], color)

    @patch('builtins.input', side_effect=['1', '7'])  # Simulamos la entrada de usuario (apostar a un número)
    def test_apostar_numero(self, mock_input):
        """Test para verificar que la función apostar() maneja correctamente una apuesta por número."""
        apuesta = Ruleta.apostar()
        self.assertEqual(apuesta['tipo'], 'numero')
        self.assertEqual(apuesta['valor'], 7)

    @patch('builtins.input', side_effect=['2', 'rojo'])  # Simulamos la entrada de usuario (apostar al color)
    def test_apostar_color(self, mock_input):
        """Test para verificar que la función apostar() maneja correctamente una apuesta por color."""
        apuesta = Ruleta.apostar()
        self.assertEqual(apuesta['tipo'], 'color')
        self.assertEqual(apuesta['valor'], 'rojo')

    @patch('builtins.input', side_effect=['3', 'par'])  # Simulamos la entrada de usuario (apostar a par/impar)
    def test_apostar_par_impar(self, mock_input):
        """Test para verificar que la función apostar() maneja correctamente una apuesta por par/impar."""
        apuesta = Ruleta.apostar()
        self.assertEqual(apuesta['tipo'], 'par_impar')
        self.assertEqual(apuesta['valor'], 'par')

    def test_verificar_ganador_numero(self):
        """Test para verificar si la función verificar_ganador() detecta una apuesta ganadora por número."""
        apuesta = {'tipo': 'numero', 'valor': 7}
        numero, color = 7, 'rojo'
        self.assertTrue(Ruleta.verificar_ganador(apuesta, numero, color))

    def test_verificar_ganador_color(self):
        """Test para verificar si la función verificar_ganador() detecta una apuesta ganadora por color."""
        apuesta = {'tipo': 'color', 'valor': 'rojo'}
        numero, color = 7, 'rojo'
        self.assertTrue(Ruleta.verificar_ganador(apuesta, numero, color))

    def test_verificar_ganador_par_impar(self):
        """Test para verificar si la función verificar_ganador() detecta una apuesta ganadora por par/impar."""
        apuesta = {'tipo': 'par_impar', 'valor': 'par'}
        numero, color = 8, 'rojo'
        self.assertTrue(Ruleta.verificar_ganador(apuesta, numero, color))

        apuesta = {'tipo': 'par_impar', 'valor': 'impar'}
        numero, color = 7, 'rojo'
        self.assertTrue(Ruleta.verificar_ganador(apuesta, numero, color))

    def test_verificar_ganador_perdedor(self):
        """Test para verificar si la función verificar_ganador() detecta una apuesta perdedora."""
        apuesta = {'tipo': 'numero', 'valor': 7}
        numero, color = 10, 'rojo'
        self.assertFalse(Ruleta.verificar_ganador(apuesta, numero, color))

        apuesta = {'tipo': 'color', 'valor': 'rojo'}
        numero, color = 10, 'negro'
        self.assertFalse(Ruleta.verificar_ganador(apuesta, numero, color))

        apuesta = {'tipo': 'par_impar', 'valor': 'impar'}
        numero, color = 8, 'rojo'
        self.assertFalse(Ruleta.verificar_ganador(apuesta, numero, color))

if __name__ == '__main__':
    unittest.main()
