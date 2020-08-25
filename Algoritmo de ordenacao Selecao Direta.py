class Ordenador:
    def selecao_direta (self, lista):
        fim = len(lista)
        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto e o i-ésimo
            posicao_do_minimo = i
            
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Coloca 0 menor elemento encontrado no inicio da sub-lista
            # Para isso, troca de lugar os elementos nas posi~oes i e posicao_do-mini
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            
lista1 = ["casa", "a", "D", "c", "j", "J"]
ord = Ordenador()
ord.selecao_direta(lista1)
print(lista1)
