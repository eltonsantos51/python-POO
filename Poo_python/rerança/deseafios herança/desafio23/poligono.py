from abc import ABC,abstractmethod

class Poligono (ABC):   
    def __init__ (self,lado):
        self.qtd_lados= lado

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):  
    def __init__(self, lado):
        super().__init__(lado)
        self.qtd_lados=lado
    def perimetro(self):
        self.res_perimetro= self.qtd_lados * 4
        return self.res_perimetro

    def area(self):
        self.res_area= self.qtd_lados * self.qtd_lados
        return self.res_area

class Circulo (Poligono):  
    def __init__(self, lado):
        super().__init__(lado)

    def perimetro(self):
        self.res_raio= self.qtd_lados * 2
        self.res_perimetro= self.res_raio * 3.14
        return self.res_perimetro
    
    def area(self):
        self.raio_2= self.qtd_lados * self.qtd_lados
        self.res_area= self.raio_2 * 3.14
        return self.res_area
    



