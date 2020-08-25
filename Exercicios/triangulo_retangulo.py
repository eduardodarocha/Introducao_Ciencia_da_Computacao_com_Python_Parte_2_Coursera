'''Escreva, na classe Triangulo, o método retangulo() que 
devolve True se o triângulo for retângulo, e False caso contrário.'''

from math import pow
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def retangulo(self):
        if pow(self.a,2) == pow(self.b,2) + pow(self.c,2) or pow(self.b,2) == pow(self.a,2) + pow(self.c,2) or pow(self.c,2) == pow(self.a,2) + pow(self.b,2):
            return True
        else:
            return False
