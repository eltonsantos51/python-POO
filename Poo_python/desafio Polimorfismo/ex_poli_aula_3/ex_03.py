
class Carteira:
    def __init__(self,valor:int|float=0):
        self.__valor= valor

    def __str__(self):
        return f'valor existente na carteira {self.valor}'
    

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self,valor):
        raise PermissionError('Voce não pode auterar valor da carteira dessa forma')

    def __eq__(self, outro):
        if self.__valor == outro.__valor:
            return True
        else:
            return False

    def __iadd__(self, valor:int|float):
        self.__valor = self.__valor + valor
        return self

    def __isub__(self, valor:int|float):
        self.__valor= self.__valor - valor
        return self

    def __le__(self, valor:int|float):
        if self.__valor <= valor.__valor:
            return True

        else:
            return False

        

        