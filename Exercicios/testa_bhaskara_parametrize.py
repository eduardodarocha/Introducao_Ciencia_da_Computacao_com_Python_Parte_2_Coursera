import Bhaskara1
import pytest

class TestBhaskara:
    
#     @pytest.fixture
    def b(self):
        return Bhaskara1.Bhaskara()

t = Bhaskara1.Bhaskara()    
#     def testa_uma_raiz(self, b):
#         assert b.calcula_raizes(1, 0, 0) == (1, 0)

@pytest.mark.parametrize("a, b, c ,saida"  [
   1, 0, 0, 0
#     (1, -5, 6), (2, 3, 2)
#     ((10, 10, 10), (0)),
#     ((10, 20, 10), (1, -1)),
#     ((1, -10 , 24),(4, 6))
    ])
# @pytest.mark.parametrize("saida", [
#      (1, 0),
#      (2, 3, 2)
#      ])


def testa_Bhaskara(a, b, c, saida ):
    assert t.calcula_raizes(a, b, c) == saida
