'''Nível Avançado: Herança e Polimorfismo5. Sistema de FuncionáriosCrie uma classe base Funcionario com
nome e salario_base.
Crie a subclasse Gerente que recebe um bônus fixo.Crie a subclasse Programador que recebe um bônus 
por projeto concluído.Sobrescreva
 o método calcular_salario em cada classe filha.'''


class Funcionario:
    
    def __init__(self,nome,salario):
        self.nome=nome
        self.base_salarial=salario
    
    def calcular_salario(self):
        return self.base_salarial
        
class Gerente(Funcionario):
    def __init__(self, nome,salario):
        super().__init__(nome,salario) 
        self.bonus= 500
   
    def calcular_salario(self):
        self.sal_bonus= self.base_salarial + self.bonus
        print(f'Funcionario(a): {self.nome}\nCargo: Gerente \nSalario: {self.sal_bonus}')
        return self.sal_bonus
       

class Programador (Funcionario):
    def __init__(self, nome,salario):
        super().__init__(nome,salario)
        
    def calcular_salario(self,proj=0):
        self.projeto:int= proj
        self.bonus= self.projeto * 500
        self.sal_bonus= self.base_salarial + self.bonus
        print(f'Funcionario(a): {self.nome}\nCargo: Programador \nSalario: {self.sal_bonus}')
        return self.sal_bonus
        


t1=Gerente('danila',1600)
t1.calcular_salario()

t2=Programador('Elton',2000)
t2.calcular_salario(2)
