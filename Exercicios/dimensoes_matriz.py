'''Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e 
imprime as dimensões da matriz recebida, no formato iXj. '''

def dimensoes(matriz):
    col = len(matriz[0])
    lin = len(matriz)
    return print(str(lin) + "X" + str(col))



