def imprime_matriz(matriz):
    for i in matriz:
        for v in i:
            if v != i[len(i) - 1]:
                print(v, end=" ")
            else:
                print(v)

        
        
