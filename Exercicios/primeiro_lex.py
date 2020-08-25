def primeiro_lex(lista):
    for pal in lista:
        if lista[0] == pal:
            menor = pal
        else:
            if ord(pal[0]) < ord(menor[0]):
                menor = pal
    return menor