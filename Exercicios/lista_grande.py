from random import randint

def lista_grande(n):
    
    lista = []
    for i in range(n):
        lista.append(randint(1, 1000))
    return lista

lista_teste = lista_grande(50)
print(lista_teste)
print(len(lista_teste))
print(int(len(lista_teste)/2))
