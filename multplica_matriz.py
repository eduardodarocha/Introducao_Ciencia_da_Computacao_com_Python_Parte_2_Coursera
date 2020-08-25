def multiplica_matrizes(m1, m2):
    '''Minha solução para multiplicação de matrizes'''
    matriz = []
    cont = 0
    b1 = 0
    for t in range(len(m1)): # números de linhas mat1
        linhanova = []
        for t1 in range(len(m2[0])): #números de colunas mat2
            while cont < len(m2):
                #a1 = m1[t][cont] * m2[cont][t1]
                #b1 = b1 + a1
                b1 = b1 + m1[t][cont] * m2[cont][t1] # refatorado
                cont += 1
            linhanova.append(b1)  
            cont = b1 = 0  
        matriz.append(linhanova)    
    return matriz

def mat_mul (A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B
    
    C = []
    for linha in range(num_linhas_A):
        C.append([])
        for coluna in range(num_colunas_B):
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C
                            
   
   
   
   
   
   
# mat1 = [[2,3,1], [-1, 0, 2]]
# mat2 = [[1, -2], [0, 5],[4, 1]]
# mat1 = [[5, 8, -4], [6, 9, -5],[4, 7, -2]]
# mat2 = [[2], [-3], [1]]
# mat1 = [[2,5,9], [3, 6, 8]]
mat1 = [[1, 2, 3], [4, 5, 6]]
mat2 = [[1, 2],[3, 4],[5, 6]]
# mat2 = [[2,7],[4,3],[5,2]]

#https://brasilescola.uol.com.br/matematica/multiplicacao-matrizes.htm
#
print(multiplica_matrizes(mat1, mat2))
# print(mat_mul (mat1, mat2))