import bhaskara_testavel

class TestBhaskara:

    def testa_uma_raiz(self):
        b = bhaskara_testavel.Bhaskara()
        assert b.calc_x1_x2(1, 0, 0) == (1, 0)
        
    def testa_duas_raiz(self):
        b = bhaskara_testavel.Bhaskara()
        assert b.calc_x1_x2(1, -5, 6) == (2, 3, 2)
        
    def testa_zero_raiz(self):
        b = bhaskara_testavel.Bhaskara()
        assert b.calc_x1_x2(10, 10, 10) == (0)
        
    def testa_raiz_negativa(self):
        b = bhaskara_testavel.Bhaskara()
        assert b.calc_x1_x2(10, 20, 10) == (1, -1)
        
# b = TestBhaskara()
# print(b())