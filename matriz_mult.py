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
