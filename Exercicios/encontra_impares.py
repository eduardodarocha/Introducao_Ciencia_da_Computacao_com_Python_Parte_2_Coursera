'''Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), 
que recebe como parâmetro uma lista de números inteiros e devolve 
uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.'''

def encontra_impares(lista):
    lista1 = []
    if len(lista) >= 1:
        if lista[0] % 2 != 0:
            lista1.append(lista[0])
        lista1 = lista1 + encontra_impares(lista[1:])
    return lista1
