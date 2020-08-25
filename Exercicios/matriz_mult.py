'''Duas matrizes são multiplicáveis se o número de colunas da primeira 
é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) 
que recebe duas matrizes como parâmetro e devolve True se as matrizes 
forem multiplicavéis (na ordem dada) e False caso contrário.'''

def dimensoes(matriz, lc):
    col = len(matriz[0])
    lin = len(matriz)
    if lc == "c":
        return col
    elif lc == "l":
        return lin
    
    
def sao_multiplicaveis(m1, m2):
    if dimensoes(m1, "c") == dimensoes(m2, "l"):
        return True
    else:
        return False
