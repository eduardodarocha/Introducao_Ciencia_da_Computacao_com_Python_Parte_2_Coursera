import ordenador
import time

class ContaTempo_1:
    def lista_aleatorio(self, n):
        from random import randrange
        lista = [randrange(0, 1000) for x in range(n)]
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatorio(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador()
        
        print('Comparando com lista aleatórias')        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'O tempo de ordenação da função bolha_curta() foi {depois - antes} segundos')

        antes1 = time.time()
        o.selecao_direta(lista2)
        depois1 = time.time()
        print(f'O tempo de ordenação da função selecao_direta() foi {depois1 - antes1} segundos')
        
        
        print('=-' * 30)
        print('Comparando com lista quase ordenadas')
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'O tempo de ordenação da função bolha_curta() foi {depois - antes} segundos')
        
        antes1 = time.time()
        o.selecao_direta(lista2)
        depois1 = time.time()
        print(f'O tempo de ordenação da função selecao_direta() foi {depois1 - antes1} segundos')
        print()
        
c = ContaTempo_1()
c.compara(1000)
c.compara(5000)