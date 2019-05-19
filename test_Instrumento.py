from unittest import TestCase
from Instrumento import Instrumento

class TestInstrumento(TestCase):
    def test_cantidad(self):
        dado = Instrumento('Guitarra', 'IV', 'Blues', 'B')
        espero = 'Guitarra cuenta con 5 ejemplares'
        resultado = dado.cantidad(5)
        self.assertEqual(espero, resultado)

        dado = Instrumento('Tambor', 'I', 'Jazz', 'F')
        espero = 'Tambor cuenta con 6 ejemplares'
        resultado = dado.cantidad(6)
        self.assertEqual(espero,resultado)

        dado = Instrumento('Violin', 'IV', 'Clacisa', 'D')
        self.assertRaises(ValueError, dado.cantidad, -5)