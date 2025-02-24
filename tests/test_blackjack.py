import unittest
import sys
import os

from unittest.mock import patch
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Blackjack
def obtenerValorCarta(carta, jugada):
    if carta == 1:
        return 11 if jugada + 11 <= 21 else 1
    return carta

class TestBlackjack(unittest.TestCase):
    def test_obtener_valor_carta(self):
        self.assertEqual(obtenerValorCarta(1, 10), 11)
        self.assertEqual(obtenerValorCarta(1, 11), 1)
        self.assertEqual(obtenerValorCarta(5, 10), 5)
    
    @patch('builtins.input', side_effect=['2', 'n'])  # Se queda y luego dice "no" a jugar de nuevo
    @patch('random.randint', side_effect=[10, 10, 10, 1])  # Controla las cartas generadas
    def test_usuario_gana(self, mock_randint, mock_input):
        from io import StringIO

        output = StringIO()
        original_stdout = sys.stdout  # Guardar stdout original
        sys.stdout = output
        
        try:
            Blackjack.juegoBlackjack()
        finally:
            sys.stdout = original_stdout  # Restaurar stdout
        
        self.assertIn("Has ganado", output.getvalue())
    
    @patch('builtins.input', side_effect=['1', '2', 'n'])  # Usuario pide carta, luego se queda y finalmente dice que no a jugar de nuevo 
    @patch('random.randint', side_effect=[10, 10, 10, 10, 6])  # Cartas predefinidas
    def test_usuario_pierde(self, mock_randint, mock_input):
        from io import StringIO
        import sys
        
        output = StringIO()
        sys.stdout = output
        
        Blackjack.juegoBlackjack()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn("has perdido", output.getvalue())
    
if __name__ == '__main__':
    unittest.main()
