from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,nome):
        self.nome=nome
        

    @abstractmethod
    def som(self):
        pass

class Pato(Animal):
    def  __init__(self, nome):
        super().__init__(nome)

    def som(self):
        return f'O {self.nome} faz Qua Qua Qua'


class Cachorro (Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        return  f'O {self.nome} faz Au Au AU'

class Gato (Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        return  f'O {self.nome} faz miau miau'
    

