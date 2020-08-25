def conta_letras(frase, contar="vogais"):
    cont = 0
    frase = frase.replace(' ', '')
    if contar == "vogais":        
        for l in frase:
            if l in 'aeiou' or l in 'AEIOU':
                cont +=1
        return cont
    else:
        for l in frase:
            if l not in 'aeiou' and l not in 'AEIOU':
                cont +=1
        return cont
