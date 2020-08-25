'''Ainda na classe Triangulo, escreva um método semelhantes(triangulo) 
que recebe um objeto do tipo Triangulo como parâmetro e verifica se o 
triângulo atual é semelhante ao triângulo passado como parâmetro. 
Caso positivo, o método deve devolver True. Caso negativo, deve devolver False.
Verifique a semelhança dos triângulos através do comprimento dos lados.
Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def semelhantes(self,t):
        lista1 = sorted([t.a, t.b, t.c])
        lista2 = sorted([self.a, self.b, self.c])
        if (lista1[0]/lista2[0]) == (lista1[1]/lista2[1]) == (lista1[2]/lista2[2]):
            return True
        else:
            return False
