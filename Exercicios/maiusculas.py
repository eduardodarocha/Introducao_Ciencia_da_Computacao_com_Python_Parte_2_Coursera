'''Escreva a função maiusculas(frase) que recebe uma frase (uma string) 
como parâmetro e devolve uma string com as letras maiúsculas 
que existem nesta frase, na ordem em que elas aparecem.
Para resolver este exercício, pode ser útil verificar uma tabela ASCII, 
que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII
Note que para simplificar a solução do exercício, as frases passadas 
para a sua função não possuirão caracteres que não estejam presentes 
na tabela ASCII apresentada, como ç, á, É, ã, etc. '''

def maiusculas(frase):
    frasefinal = ""
    for l in frase:
        if 65 <= ord(l) <= 90:
            frasefinal += l
    return frasefinal        
