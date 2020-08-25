import pytest

# fatorial!
def fatorial (n):
    if n < 0:
        return 0
#     if n == 1 or n == 0:
#         return 1
    fat = 1
    cont = n
    while cont >= 1:
        fat = fat * cont
        cont -= 1
    return fat


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120),
    (15, 1307674368000)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
