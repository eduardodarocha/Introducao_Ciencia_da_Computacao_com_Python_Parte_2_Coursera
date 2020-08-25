class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        return lista
            
    def bolha(self, lista):
        fim = len(lista)
        for i  in range (fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def bolha_curta(self, lista): #Algoritmo bolha melhorado
        fim = len(lista)
        for i  in range (fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return
        return lista
    
    def ordenacao_insercao(self, lista):
        for i in range(1, len(lista)):
            tamlista = i
            key = lista[i]
            while tamlista > 0 and key < lista[tamlista - 1]:
                lista[tamlista] = lista[tamlista - 1]  
                tamlista -= 1
            lista[tamlista] = key
        return lista
    

            
    