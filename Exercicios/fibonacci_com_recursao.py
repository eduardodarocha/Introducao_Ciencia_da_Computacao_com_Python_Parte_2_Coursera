def fibonacci(n):
    if n < 2:            # base da recursão 
        return n
    else:
        return fibonacci(n -1) + fibonacci(n - 2) #chamada recursiva
    
import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21)
    ])
def testa_finonacci(entrada,esperado):
    assert fibonacci(entrada) == esperado