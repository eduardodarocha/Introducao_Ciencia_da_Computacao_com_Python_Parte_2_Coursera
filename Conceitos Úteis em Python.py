# x, y, z = 2, 4, 6
# print(x, y, z)
# def peso_alt():
#     return 75, 1.75
# 
# peso, altura = peso_alt()
# print(f'Meu peso é {peso} e minha altura é {altura}')
# 
# a = 10
# b = 21
# print(a, b)
# a, b = b, a
# print(a, b)

# def pagamento_semanal(valor_por_hora, num_horas = 40):
#     return valor_por_hora * num_horas
# 
# print(pagamento_semanal(100))

def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >=0 and num_horas > 0
        
    return valor_por_hora * num_horas

print(pagamento_semanal(100, -35))

def calculo(x, y = 10, z = 5):
    return x + y * z;
#print(calculo(7,2))
# 
# print(calculo(1, 2, 3))#, o código irá imprimir 7
# 
# print(calculo(7))#, o código irá imprimir 57
# 
# print(calculo())#, o código dará TypeError: calculo() missing 1 required positional argument: 'x'
# 
#print(calculo( ,12, 10))#, o código dará SyntaxError: invalid syntax
# 
print(calculo(7, 2))#, o código irá imprimir 17

