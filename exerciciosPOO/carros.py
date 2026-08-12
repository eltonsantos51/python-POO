'''Locadora de VeículosCrie uma classe abstrata Veiculo com método calcular_aluguel(dias).
 Implemente a classe Carro (cobrança fixa por dia).
Implemente a classe Moto (cobrança por dia com 10% de desconto).'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self):
        self.preco=0
    @abstractmethod
    def calcular_aluguel(self,dias):
        pass

class Carro(Veiculo):
    def __init__(self):
        super().__init__()       
        self.preco=100

    def calcular_aluguel(self,dias):
                
        valor= dias * self.preco
        print(valor)
        return valor
    
class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        
        self.preco=50
    def calcular_aluguel(self,dias):
        
        valor= dias * self.preco
        desc= valor * (10 / 100)
        res= valor - desc
        print(res)
        return res

celta=Carro()
celta.calcular_aluguel(10)

fazer= Moto()
fazer.calcular_aluguel(20)



