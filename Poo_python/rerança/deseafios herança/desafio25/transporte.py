from abc import ABC, abstractmethod
class CalcularFrete (ABC):
    def __init__(self,distancia):
        self.distancia= distancia
        
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(CalcularFrete):
    fator=0.50  
    def calc_frete(self):
       self.calc_frete= self.distancia * self.fator
       return f'R${(self.calc_frete):.2f}'
    
class Caminhao(CalcularFrete):
    fator=1.20 
    
    def calc_frete(self):
        if self.distancia  > 50:
            self.calc_frete= self.distancia * self.fator
            return f'R${(self.calc_frete):.2f}'
        else:
            return f'Raio raio minimo de 50km '

class Drone(CalcularFrete):
    fator=9.50
    def calc_frete(self):
        if self.distancia <=10:
            self.calc_frete= self.distancia * self.fator
            return f'R${(self.calc_frete):.2f}'
        else:
            return f' Raio raio maximo de 10km '

