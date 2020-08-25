'''Implemente a função bubble_sort(lista), que recebe uma 
lista com números inteiros como parâmetro e devolve esta 
lista ordenada. Utilize o algoritmo bubble sort.
Além de devolver uma lista ordenada, ao longo do 
processamento sua função deve imprimir o estado atual da 
lista toda vez que fizer uma alteração em seus elementos.'''

def bubble_sort(lista):
    fim = len(lista)
    for i  in range (fim - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    return lista
