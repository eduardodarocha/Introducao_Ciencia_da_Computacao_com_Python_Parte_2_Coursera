import ordenador
import time

class ContaTempo:
    def lista_aleatorio(self, n):
        from random import randrange
        lista = [0 for x in range(n)]
        for i in range (n):
            lista[i] = randrange(0, 1000)
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatorio(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print(f'O tempo de ordenação da função bolha() foi {depois - antes} segundos')

        antes1 = time.time()
        o.selecao_direta(lista2)
        depois1 = time.time()
        print(f'O tempo de ordenação da função selecao_direta() foi {depois1 - antes1} segundos')

c = ContaTempo()
c.compara(1000)
c.compara(5000)
    

    
    