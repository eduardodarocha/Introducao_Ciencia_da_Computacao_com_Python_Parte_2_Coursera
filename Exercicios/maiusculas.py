def maiusculas(frase):
    frasefinal = ""
    for l in frase:
        if 65 <= ord(l) <= 90:
            frasefinal += l
    return frasefinal        
