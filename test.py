import unittest
from app import dni_valido, calcular_ganador, calcular_votos

class TestCalculaGanador(unittest.TestCase):

    def test_dni_valido(self):
        self.assertTrue(dni_valido("12345678", "1"))
        self.assertFalse(dni_valido("1234567", "1"))
        self.assertFalse(dni_valido("12345678", "0"))

    def test_calcular_ganador(self):
        datos = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        resultado = calcular_ganador(datos)
        self.assertEqual(resultado, ['Aundrea Grace'])

    def test_calcular_votos(self):
        archivo = '0204.csv'  
        resultado = calcular_votos(archivo)
        self.assertEqual(resultado, ['Aundrea Grace'])

if __name__ == '__main__':
    unittest.main()
