'''Defina a classe Triangulo cujo construtor recebe 3 valores 
inteiros correspondentes aos lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perimetro, 
que não recebe parâmetros e devolve um valor inteiro 
correspondente ao perímetro do triângulo.'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
