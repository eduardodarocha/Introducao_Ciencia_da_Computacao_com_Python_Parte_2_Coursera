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
