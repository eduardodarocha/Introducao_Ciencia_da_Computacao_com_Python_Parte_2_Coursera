def menor_nome(nomes):
    for n in nomes:
        n = n.strip()
        if nomes[0].strip() == n:
            menor = n
        else:
            if len(n) < len(menor):
                menor = n
    return menor.capitalize()
