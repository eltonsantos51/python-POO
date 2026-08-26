from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod
    def analisar(self,valor):
        print(f'Não foi possivel analisar valor {valor}')
    @analisar.register
    def nalisar_(self,valor:int):
        print(f'O valor {valor} é inteiro')

    @analisar.register
    def analisar_(self,valor:float):
        print(f'O valor {valor} é um ponto flutuante (real) ')

    @analisar.register
    def analisar_(self,valor:list|tuple|dict):
        print(f'O valor {valor} é uma coleção')
    @analisar.register
    def analisar_(self,valor:str):
        print(f'O valor {valor} é uma sequencia de caracteres')

