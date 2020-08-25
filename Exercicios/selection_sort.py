'''Implemente a função ordena(lista), que recebe uma lista com 
números inteiros como parâmetro e devolve esta lista ordenada 
em ordem crescente. Utilize o algoritmo selection sort.'''

def ordena(lista):
    for i in range(len(lista) - 1):
        pos_min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[pos_min]:
                pos_min = j
        lista[i], lista[pos_min] = lista[pos_min], lista[i]
    
    return lista

print(ordena([38, 73, 20, 82, 28, 33, 49, 97, 75, 32, 37, 23, 5, 5, 99, 45, 86, 38, 18, 3, 99, 48, 85, 38, 72]))