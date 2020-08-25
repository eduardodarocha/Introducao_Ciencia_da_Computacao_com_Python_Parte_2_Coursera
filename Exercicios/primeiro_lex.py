'''Escreva a função primeiro_lex(lista) que recebe uma lista de strings 
como parâmetro e devolve o primeiro string na ordem lexicográfica. 
Neste exercício, considere letras maiúsculas e minúsculas. '''

def primeiro_lex(lista):
    for pal in lista:
        if lista[0] == pal:
            menor = pal
        else:
            if ord(pal[0]) < ord(menor[0]):
                menor = pal
    return menor