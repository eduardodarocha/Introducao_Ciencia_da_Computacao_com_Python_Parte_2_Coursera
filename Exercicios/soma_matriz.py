def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz = []
        for t in range(len(m1)):
            linhanova = []
            for t1 in range(len(m1[0])):
                linhanova.append(m1[t][t1] + m2[t][t1])
            matriz.append(linhanova)
        return matriz
    else:
        return False


def dimensoes(matriz):
    col = len(matriz[0])
    lin = len(matriz)
    return lin, col

# if __name__ == '__main__':
#     m1 = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 9]]
#     m2 = [[10, 20, 30, 40], [40, 50, 60, 70], [70, 80, 90, 90]]
#     print(soma_matrizes(m1, m2))