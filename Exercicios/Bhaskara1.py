import math
import pytest

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c
    
    def main(self):
        a_digitado = float(input("Digte o valor de a: "))
        b_digitado = float(input("Digte o valor de b: "))
        c_digitado = float(input("Digte o valor de c: "))
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))
        
    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2
            
# 
# t = Bhaskara()
# @pytest.mark.parametrize("entrada, saida", [
#     ((1, 0, 0), (1, 0)),
#     ((1, -5, 6), (2, 3, 2)),
#     ((10, 10, 10), (0)),
#     ((10, 20, 10), (1, -1)),
#     ((1, -10 , 24),(4, 6))
#     ])
# 
# 
# def testa_Bhaskara(entrada):
# 
#     assert t.calcula_raizes(entrada[0],entrada[1], entrada[2]) == saida