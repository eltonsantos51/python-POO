
#classe
class carros:
    ''' Essa classe mostra os nomes de carros com seus valores anos e calcula seu ipva no final 
        para cadastrar novos carros adicione uma variavel = carros ('nome', valor, ano)
    '''
    def __init__(self,nome,valor,ano):
        #atributo
        self.nome=nome
        self.valor=valor
        self.ano=ano
    #metodos   
    def preco_ipva(self):
        self.ipva= (self.valor* 4) /100
    #instancia 
    def __str__(self):
        return f'carro:{self.nome}\nvalor:{self.valor}\nano:{self.ano}\nipva:{self.ipva}'
    
    def __getstate__(self):
        return f'carro={self.nome}:valor={self.valor}:ano={self.ano}:ipva={self.ipva}'
    
    
#objeto 1
carro_1= carros('gol',15000,2008)
carro_1.preco_ipva()
print(carro_1)
print(carro_1.__getstate__())
print('')
carro_2= carros('elantra',70000,2017)
carro_2.preco_ipva()
print(carro_2)
print(carro_2.__getstate__())

print('')
carro_3= carros('corola',150000,2022)
carro_3.preco_ipva()
print(carro_3)
print(carro_3.__getstate__())

