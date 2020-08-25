'''Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao n-ésimo elemento da sequência
de Fibonacci. Sua solução deve ser implementada utilizando recursão.'''

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
