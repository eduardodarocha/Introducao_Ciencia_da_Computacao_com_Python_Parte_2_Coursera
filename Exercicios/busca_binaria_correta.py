def sort_list(lista):
    for i in range(len(lista) - 1):
        posicao_do_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return lista

def busca_binaria(lista, x):  # não retorna a posiçao correta do elemento na lista
    lista1 = sort_list(lista) # só retorna se ele existe na lista
    mid_list = len(lista1)
    while mid_list != 0:
        mid_list = len(lista1)
        mid_list = mid_list // 2
        if lista1[mid_list] == x:
            return mid_list
        elif lista1[mid_list] > x:
            lista1 = lista1[:mid_list]
        elif lista1[mid_list] < x:
            lista1 = lista1[mid_list:]
    return

def busca_binaria_c(lista, x):
    lista = sort_list(lista)
    primeiro = 0
    ultimo = len(lista) - 1
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return -1  


lista_teste = [45, 86, 12, 37, 52, 95, 99, 16, 80]#, 70, 49, 45, 48, 42, 12, 12, 34, 80, 28, 67, 38, 43, 36, 69, 72, 22, 54, 74, 67, 85, 1, 25, 92, 85, 59, 59, 37, 78, 26, 71, 19, 50, 79, 8, 57, 66, 58, 18, 77, 10, 35]
print(busca_binaria_c(lista_teste, 45))