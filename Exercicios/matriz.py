def cria_matriz(num_linhas, num_colunas, valor):
    '''Cria e retorna uma matriz com num_linhas linhas e
        num_colunas colunas e em cada elemento é igual ao
        valor dado'''
    matriz = []
    linha = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz     

print(cria_matriz(5, 8, 0))
