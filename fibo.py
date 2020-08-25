def fib(n):
    '''Calcula e imprime os valores da sequência
    de Fibonacci até o valor n.'''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):
    '''Calcula e retorna os valores da sequência
    de Fibonacci até o valor n.'''
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
