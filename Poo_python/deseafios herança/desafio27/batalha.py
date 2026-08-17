from abc import ABC, abstractmethod
from rich import print
import random

class Personagem (ABC):
    def __init__(self,nome,vida):
        self.nome=nome
        self.vida=vida
        self.golpe=[]

    def atacar(self, alvo,forca):
        self.foca=forca
        self.alvo=alvo
        n=0
        self.ataque= random.randint(n,self.foca)
        return print(f'O[green] {self.nome}[/][blue]({self.vida})[/] atacou [red] {self.alvo.nome}[/] [blue] ({self.alvo.vida})[/] com um[yellow] {self.res_golpe} [/] de foca [pink] {self.foca}[/]. \n'
                     f'[blue]{self.alvo.nome}[/] recebeu dano de[red] {self.ataque}[/]!'  )
                      
    @abstractmethod
    def cura(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        
    def atacar(self, alvo, forca):
        self.golpe=['soco','chute giratorio','espadada']
        self.res_golpe= random.choice(self.golpe)
        super().atacar(alvo, forca)
        return self.res_golpe
        
    def cura(self):
        c=0
        self.cura= random.randint(c,100)
        return print(f'[blue]{self.nome}[/] fez uma atadura e conseguiu [red] {self.cura}[/] de vida ')

class Mago (Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
          
    def atacar(self, alvo, forca):
        self.golpe=['bola de fogo','raios de choque','bola de plasma' ]
        self.res_golpe= random.choice(self.golpe)
        super().atacar(alvo, forca)
        return self.res_golpe
    
    def cura(self):
        c=0
        self.cura= random.randint(c,100)
        return print(f'[blue]{self.nome}[/] fez uma poção[red] {self.cura} [/] de vida ')






        