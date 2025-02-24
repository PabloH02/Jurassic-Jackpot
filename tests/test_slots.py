import unittest
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Slots

class TestJuegoSlots(unittest.TestCase):

    # Test para verificar que girar los carretes devuelve una combinación de tres símbolos
    def test_girar_carretes(self):
        # Usamos carretes predecibles para la prueba
        carrete_1, carrete_2, carrete_3 = Slots.girar_carretes(["🍒", "🍒", "🍒"])
        
        # Verificamos que los tres carretes sean iguales
        self.assertEqual(carrete_1, carrete_2)
        self.assertEqual(carrete_2, carrete_3)
        self.assertEqual(carrete_1, "🍒")
        
        # Comprobamos que la función pueda también devolver resultados aleatorios sin error
        carrete_1, carrete_2, carrete_3 = Slots.girar_carretes()
        self.assertIn(carrete_1, Slots.simbolos)
        self.assertIn(carrete_2, Slots.simbolos)
        self.assertIn(carrete_3, Slots.simbolos)

    # Test para verificar la función que determina si hay un ganador
    def test_es_ganador(self):
        # Caso ganador (todos los carretes son iguales)
        self.assertTrue(Slots.es_ganador("🍒", "🍒", "🍒"))
        
        # Caso no ganador (los carretes son diferentes)
        self.assertFalse(Slots.es_ganador("🍒", "🍋", "🍇"))
    
    # Test para verificar la función de mostrar resultados (capturamos la salida estándar)
    def test_mostrar_resultados(self):
        # Redirigimos la salida a un StringIO para capturarla
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Llamamos a la función mostrar_resultados con un ejemplo de carretes
        Slots.mostrar_resultados("🍒", "🍒", "🍒")
        
        # Comprobamos que la salida sea la esperada
        self.assertEqual(captured_output.getvalue().strip(), "🍒 | 🍒 | 🍒")
        
        # Restauramos la salida estándar
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()
