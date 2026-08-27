from abc import ABC,abstractmethod
class Funcionario(ABC):
    def __init__(self,nome:str,salario:float):
        self.nome=nome 
        self.__salario=salario
        self.sal_bonus=0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,valor):
        if valor >self.__salario:
            self.__salario=valor
        else:
            raise PermissionError('voce não pode mexer no salario dessa forma')
    @abstractmethod
    def calcular_bonus(self):
        pass

   


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
     
        

    def calcular_bonus(self):
        self.sal_bonus= (self.salario*10)/100
        return self.sal_bonus

    def __str__(self):
        return f'{self.nome} ganha {self.salario:.2f} e por ser {__class__.__name__} o bonus sera de {self.  calcular_bonus():.2f}'

         


class Desing(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        self.sal_bonus= (self.salario*8)/100
        return self.sal_bonus
    def __str__(self):
        return f'{self.nome} ganha {self.salario:.2f} e por ser {__class__.__name__} o bonus sera de {self.  calcular_bonus():.2f}'


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        


    def calcular_bonus(self):
        self.sal_bonus= (self.salario*15)/100
        return self.sal_bonus
        
    def __str__(self):
        return f'{self.nome} ganha {self.salario:.2f} e por ser {__class__.__name__} o bonus sera de {self.  calcular_bonus():.2f}'
    

