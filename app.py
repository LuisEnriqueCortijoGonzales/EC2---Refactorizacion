import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
##region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)

#Se creo la funcion dni_valido que elimina codigo duplicado, pensando en escalamiento del codigo.
def dni_valido(dni, es_valido):
        if len(dni) == 8 and es_valido == '1':
            return True
        else:
            return False
        
class CalculaGanador:


    #Se refactorizaron los nombres de las variables  a un solo idioma (español)  y se agregaron
    # los _ para separar los nombres
    def leer_datos(self):
        datos = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datos_a_leer = csv.reader(csvfile)
            for fila in datos_a_leer:
                datos.append( fila)
        return datos
    
    
    #Se refactorizo la funcion calcular_ganador cambiando sus condicionales a los atributos del csv
    #con fines de escalamiento y mejor comprencion por parte del lector, en lugar de la implementacion por indices.
    def calcular_ganador(self, datos):
        votos_x_candidato = {}
        total_votos_validos = 0

        for fila in datos:
            region, provincia, distrito, dni, candidato, es_valido = fila
            if dni_valido(dni, es_valido):
                total_votos_validos += 1
                if candidato not in votos_x_candidato:
                    votos_x_candidato[candidato] = 0
                votos_x_candidato[candidato] += 1
                #Se simplificaron las condicionas en todas las funciones haciendolas lo mas comprencible posible
        candidatos_ganadores = [candidato for candidato, votos in votos_x_candidato.items() if votos / total_votos_validos > 0.5]

        if candidatos_ganadores:
            return [candidatos_ganadores[0]]
        else:
            candidatos_ordenados = sorted(votos_x_candidato, key=lambda candidato: (-votos_x_candidato[candidato], candidato))
            return candidatos_ordenados[:2]
        
    #la funcion calcular votos aprovecha las funciones ya hechas para no redundar el codigo
    def calcular_votos(self):
        datos = self.leer_datos()
        ganador = self.calcular_ganador(datos)
        return ganador

c = CalculaGanador()
resultado = c.calcular_votos()
print (resultado)

#se movio el test a otro archivo para mejor orden

#Para la entrega añado el comentario con el archivo test.py

'''
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

'''

#Total de tecnicas utilizadas de refactorizacion: 5