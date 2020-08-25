def cria_matriz(num_linhas, num_colunas):
    '''Cria, lê e retorna uma matriz com num_linhas linhas e
        num_colunas colunas e em cada elemento é igual ao
        valor digitado pelo usuário'''
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas): 
            valor = int(input(f'Digite o elemento [{i}][{j}] da matriz'))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Digite o número de colunas: '))
    return cria_matriz(lin, col)

print(le_matriz())
