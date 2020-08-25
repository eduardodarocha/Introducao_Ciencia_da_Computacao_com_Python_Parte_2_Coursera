'''Na classe triângulo, definida no exercício Classe triângulo, escreva 
o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:
isósceles (dois lados iguais)
equilátero (todos os lados iguais)
escaleno (todos os lados diferentes)
Note que se o triângulo for equilátero, a função não deve devolver isóceles.'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.c != self.b:
            return 'escaleno'
        elif self.a == self.b != self.c or self.a == self.c != self.b or self.b == self.c != self.a:
            return 'isósceles'
