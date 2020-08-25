class Ordenador:
    
    def bolha(self, lista):
        fim = len(lista)
        for i  in range (fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        
            
lista1 = ["casa", "a", "D", "c", "j", "J"]
lista2 = [10, 3, 8, -10, 200, 17, 32]

ord = Ordenador()
ord.bolha(lista2)
print(lista2)
