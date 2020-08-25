'''Escreva uma função imprime_matriz(matriz), que recebe uma matriz 
como parâmetro e imprime a matriz, linha por linha. Note que NÃO se 
deve imprimir espaços após o último elemento de cada linha!'''

def imprime_matriz(matriz):
    for i in matriz:
        for v in i:
            if v != i[len(i) - 1]:
                print(v, end=" ")
            else:
                print(v)
