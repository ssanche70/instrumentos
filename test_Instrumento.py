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

    def test_cuerdas(self):
        dado = Instrumento('Violin', 'I', 'Jazz', 'F')
        espero = 'Violin tiene 4 cuerdas y estan afinadas en FBAD respectivamente'
        resultado = dado.cuerdas(4, 'FBAD')
        self.assertEqual(espero, resultado)

        dado = Instrumento('Arpa', 'I', 'Jazz', 'F')
        espero = 'Arpa tiene 19 cuerdas y estan afinadas en FBADCGDBAFACBCDEDGA respectivamente'
        resultado = dado.cuerdas(19, 'FBADCGDBAFACBCDEDGA')
        self.assertEqual(espero, resultado)

        dado = Instrumento('Viola', 'I', 'Jazz', 'F')
        self.assertRaises(ValueError, dado.cuerdas, -4, 'FBAD')

    def test_percusion(self):
        dado = Instrumento('Timbal', 'V', 'Caribe', 'B')
        espero = 'Timbal tiene un diametro de 25 cm y una frecuencia de vibracion de 40 Hz'
        resultado = dado.percusion(25, 40)
        self.assertEqual(espero, resultado)

        dado = Instrumento('Caja', 'VI', 'Vallenato', 'C')
        self.assertRaises(ValueError, dado.percusion, -45, 2)

        dado = Instrumento('Caja', 'VI', 'Vallenato', 'C')
        self.assertRaises(ValueError, dado.percusion, 45, -2)