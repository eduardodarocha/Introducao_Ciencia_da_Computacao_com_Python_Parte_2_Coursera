'''Implemente a função insertion_sort(lista), que recebe 
uma lista com números inteiros como parâmetro e devolve
 esta lista ordenada. Utilize o algoritmo insertion sort.'''
 
def insertion_sort(lista):
    for i in range(1, len(lista)):
        tamlista = i
        key = lista[i]
        while tamlista > 0 and key < lista[tamlista - 1]:
            lista[tamlista] = lista[tamlista - 1]  
            tamlista -= 1
            print(lista)
        lista[tamlista] = key
    return lista 
