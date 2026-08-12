from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print
class Funcionario (ABC):
    
    def __init__(self,nome):
        self.nome=nome
        self.sal_bruto=0
        self.salario=0
        self.sal_min= 1612
        self.inss= 0.075

    @abstractmethod
    def calc_sal(self):
        pass

    @abstractmethod
    def analisar_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self,nome,valo_h,h_trab ):
        super().__init__(nome)
        self.valor_hora= valo_h
        self.hora_trab=h_trab
    
    def calc_sal(self):
        self.total_sal= self.valor_hora * self.hora_trab
        self.res_sal= self.total_sal * (1 - self.inss)
        return(self.res_sal)
    
    def analisar_sal(self):
        self.analisar= self.calc_sal() / self.sal_min
        conteudo= f'O salario de [red] {self.nome}[/] [blue] ({self.__class__.__name__})[/] é de [green] R${self.calc_sal():.2f}[/]'
        conteudo += f' e correponde a [yellow] {self.analisar:.1f} salarios minimos[/].'
        resultado= Panel (f'{conteudo}',title='Analisar salario', width=35)
        return print(resultado)

class Mensalista (Funcionario):
    def __init__(self, nome,salario_brut):
        super().__init__(nome)
        self.sal_bruto= salario_brut
   
    def calc_sal(self):
        self.total_sal= self.sal_bruto * (1-self.inss)
        return self.total_sal
    
    def analisar_sal(self):
        self.analisar= self.total_sal / self.sal_min
        conteudo= f'O salario de [red]{self.nome}[/] [blue] ({self.__class__.__name__})[/] é de [green] R${self.calc_sal():.2f} [/] '
        conteudo += f' e correponde a [yellow] {self.analisar:.1f} salarios minimos.[/]'
        resultado= Panel (f'{conteudo}',title='Analisar salario', width=35)
        return print(resultado)

