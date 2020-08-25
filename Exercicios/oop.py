# class Carro:
#     pass
# 
# meu_carro = Carro()
# carro_do_ime = Carro()
# 
# meu_carro.ano =1968
# meu_carro.modelo = 'Fusca'
# meu_carro.cor = 'azul'
# 
# carro_do_ime.ano = 1981
# carro_do_ime.modelo = 'Brasília'
# carro_do_ime.cor = 'amarelo'

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
carro_do_meu_avo = Carro('Ferrari', 1975, 'vermelho')
print(carro_do_meu_avo.cor)



# print(meu_carro.ano)