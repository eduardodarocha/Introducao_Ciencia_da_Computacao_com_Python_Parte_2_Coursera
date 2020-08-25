#class Ordenador:
def ordenacao_insercao(lista): #(self, lista):
    for i in range(1, len(lista)):
        for j in range(len(lista[0:i])):
            if lista[i] < lista[j]:
                lista[i] , lista[j] = lista[j], lista[i]
            
        



lista = [42, 82, 66, 24, 29, 33, 34, 83, 35, 90, 92, 9, 4, 26, 54, 80, 12, 40, 2, 88, 99, 49, 63, 16, 32, 40, 74, 50, 67, 99, 60, 53, 55, 49, 23, 23, 73, 63, 65, 51, 30, 38, 7, 90, 23, 35, 11, 59, 67, 92]
print(len(lista))
ordenacao_insercao(lista)
print(lista)
print(len(lista))

