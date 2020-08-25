def ordenada(lista):
    fim = len(lista)
    saida = True
    for i in range(fim - 1):
        posicao_do_minimo = i
        
        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
                return False
            else:
                saida = True
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return saida
