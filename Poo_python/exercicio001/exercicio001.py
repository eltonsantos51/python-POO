#classe
class carros:
    #atributo
    def __init__(self):
        self.nome=''
        self.valor=0
        self.ano=0
    #metodos   
    def preco_ipva(self):
        self.ipva= (self.valor* 4) /100
    #instancia 
    def resultado(self):
        return f'carro:{self.nome}\nvalor:{self.valor}\nano:{self.ano}\nipva:{self.ipva}'
    
#objeto 1
carro_1= carros()
carro_1.nome='gol'
carro_1.valor=15000
carro_1.ano=2008
carro_1.preco_ipva()
print(carro_1.resultado())
print('')

carro_2= carros()
carro_2.nome='elantra'
carro_2.valor=70000
carro_2.ano=2017
carro_2.preco_ipva()
print(carro_2.resultado())
print('')
carro_3= carros()
carro_3.nome='corola'
carro_3.valor=150000
carro_3.ano=2022
carro_3.preco_ipva()
print(carro_3.resultado())