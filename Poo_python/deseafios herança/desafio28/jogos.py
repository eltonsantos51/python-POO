'''
class ContaBancaria:
    def __init__(self,conta=0,nome='',saldo=0.0):
        self.numero_conta=conta
        self.nome=nome
        self.saldo=saldo

    
    def depositar(self,dep=0.0):
        if dep > 0:
            self.saldo= dep + self.saldo
            print(f'Deposito de {dep:.2f} efetuado com sucesso\nSaldo atual:{self.saldo:.2f}')
            return self.saldo         
        else:
            print(f'Operação invalida!!')
        
    def sacar(self,saq=0):
        
        if saq <=0:
           print('Operação invalida')
        elif saq <= self.saldo:
            self.saldo= self.saldo - saq
            print(f'Saque efetuado com sucesso!!\nSaldo atual:{self.saldo:.2f}')
        else:
            print('saldo insuficinete!!')
    def __str__(self):
        return f'Conta criada com sucesso!!\nConta:{self.numero_conta}\nNome:{self.nome}\nSaldo:{self.saldo:.2f}'
'''
'''
from rich import print,emoji
class funcionario:
    empresa='E & D tec'
    def __init__(self,nome,setor,cargo):
        self.nome=nome
        self.setor=setor
        self.cargo=cargo
    def apresentação(self):
        return f':victory_hand: ola, sou[blue] {self.nome}[/] sou {self.cargo} do {self.setor} da {self.empresa}'
'''
'''
from rich.console import Console
from rich.panel import Panel
class produto: 
    def __init__(self,nome,preco):
        self.nome = nome 
        self.preco=preco
    def etiqueta(self):
        chamada=Console()
        painel=Panel(f'{self.nome:>18}\n{'-'*25}\n{self.preco:>15.2f}',title='Produdo',width=30)
        chamada.print(painel)
p1=produto('poco phone',1700)
p1.etiqueta()

'''
'''
from rich.console import Console
from rich.panel import Panel

class Churrasco:
    consumo_pessoa:float=0.400
    preco_carne:float=82.40
    
    def __init__(self,titulo,quant):
        self.titulo=titulo
        self.amigos=quant
    
    def compra(self):
        self.comprar_carne= self.amigos *self.consumo_pessoa
        return self.comprar_carne
    
    def valor_total_carne(self):
        self.total_carne= self.compra() * self.preco_carne
        return self.total_carne
    
    def divisao(self):
        self.divisao_cada= self.valor_total_carne() / self.amigos
        return self.divisao_cada
    
    def analisar(self):
        chamada=Console()
        conteudo=f'Analisando[red] {self.titulo}[/] com [blue] {self.amigos} convidados[/]'
        conteudo+=f'\nCada participante comerá  {self.consumo_pessoa}kg e cada kg cutas R${self.preco_carne:.2f}'
        conteudo+=f'\nRecomendo comprar[blue] {self.compra():.2f}kg[/] de carne'
        conteudo+=f'\nOcusto total sera de[green] R${self.valor_total_carne():.2f}[/]'
        conteudo+=f'\nCada pessoa pagará[yellow] R${self.divisao():.2f}[/] para participar'
        painel=Panel(conteudo,title=self.titulo,width=80)
        chamada.print(painel)

p1=Churrasco('churrasco dos amigos',15)
p1.analisar()

'''
'''
from rich import print, inspect

class Pessoa:
    def __init__(self,nome='',idade=0):
        self.nome=nome
        self.idade=idade
    
    def aniversario(self):
        self.idade+=1


class Aluno (Pessoa):
    def __init__(self, nome, idade, curso,turma):
        super().__init__(nome, idade)
        self.curso=curso
        self.turma=turma
    def fazer_matricula(self):
        print(f'O aluno a {self.nome} acabou de fazxer a metricula')


class Professor(Pessoa):
    def __init__(self, nome, idade,espe,nivel):
        super().__init__(nome, idade) 
        self.espe=espe
        self.nive=nivel

    def dar_aula(self):
        print(f'O professor {self.nome} de {self.espe} esta dando aula ')


class Funcionario(Pessoa):
    def __init__(self, nome, idade,cargo,setor):
        super().__init__(nome, idade)
        self.cargo= cargo
        self.setor=setor

    def bater_ponto(self):
        print(f'A funcionaria {self.nome} que é {self.cargo} acabou de bater ponto')

a1=Aluno('elton',30,'ads',1212)
a1.aniversario()
a1.fazer_matricula()
p1=Professor('nome',45,'TI','pos-graduado')
p1.aniversario
p1.dar_aula()
f1=Funcionario('danila',29,'secretaria','administrativo')
f1.aniversario()
f1.bater_ponto()
'''
'''
from abc import ABC, abstractmethod
import math
class Poligono(ABC):
    def __init__(self,quant):
        self.quant_lado=quant

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, quant):
        super().__init__(quant)
        self.quant_lado=quant

    def perimetro(self):
        self.valor_perimentro= 4 * self.quant_lado
        return self.valor_perimentro
    

    def area(self):
        self.valor_area= self.quant_lado * self.quant_lado
        return self.valor_area
    
class Criculo(Poligono):
    def __init__(self, quant):
        super().__init__(quant)
        self.raio=quant


    def perimetro(self):
        self.valor_perimetro= (2* math.pi)*self.raio
        return self.valor_perimetro
    
    def area(self):
        self.valor_area= (self.raio*self.raio)*math.pi
        return self.valor_area
        

p1=Criculo(20)
print(f'Perimetro= {p1.perimetro():.1f}')
print(f'area= {p1.area():.2f}')
'''
'''    
    
from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    
    def preparo(self):
        print('iniciando o preparo ')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('Bebida pronta')
    
    def ferver_agua( self):
        print('1.Fervendo agua a 100 graus celcius.')
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(sel):
        pass
    
class cafe(BebidaQuente):
    
    def misturar(self):
        print('2.Passando agua pressurizada pelo po do cafe moido')
    
    def servir(sel):
        print('3.Servindo xicara pequena')

class Cha(BebidaQuente):
   
    def misturar(self):
        print('2. Mergulhgar sache de ervas na agua.')

    def servir(sel):
        print('3. Servindo na caneca de porcelana com limão ')

class leite(BebidaQuente):
    
    def misturar(self):
        print('2. Passando vapor pressurizado pelo bicop de leite ')
    def servir(sel):
        print('3. Servindo na caneca grande ,ja com cafe ')
    
bebida=Cha()
bebida.preparo()
'''
'''
from abc import ABC,abstractmethod

class Transporte(ABC):
    def __init__(self,distan):
        self.distancia=distan
        self.frete=0
        
    @abstractmethod
    def calcular_frete(self):
        pass
class Moto(Transporte):
    fator=0.50
    def __init__(self, distan):
        super().__init__(distan)
    
    def calcular_frete(self):
        self.frete= self.distancia * self.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator=1.20
    def __init__(self, distan):
        super().__init__(distan)

    def calcular_frete(self):
        if self.distancia < 50:
            return f'Raio minimo 50km'
        else:
            self.frete= self.distancia* self.fator
            return f'R${self.frete:.2f}'
class Drone(Transporte):
    fator=9.50
    def __init__(self, distan):
        super().__init__(distan)
    
    def calcular_frete(self):
        if self.distancia > 10:
            return f' Raio maximo de 10km'
        else:
            self.frete= self.fator * self.distancia
            return f'R${self.frete:.2f}'
dist=8
entrega=Drone(dist)
print(f'Frete de {type(entrega).__name__} em {dist}km= {entrega.calcular_frete()}')
        
'''
'''
from abc import ABC, abstractmethod
from rich.panel import Panel
from rich.console import Console

class Funcionario(ABC):
    sal_min=1612
    inss=7.5
    def __init__(self,nome):
        self.nome=nome
        self.salario_bruto=0
        self.salario= 0
        self.desc=0 
    
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        self.res_analise=self.calc_sal()/self.sal_min
        quadro= Console()
        conteudo=f'O salario de {self.nome}  ({self.__class__.__name__})é de {self.calc_sal():.2f}\n'
        conteudo+=f' e corresponde á {self.res_analise:.1f} salarios minimos.'
        painel=Panel(conteudo,title='Analisar Salario',width=50)
        quadro.print(painel)

        
class Horista(Funcionario):
    def __init__(self, nome,val_hora,hora_trab):
        super().__init__(nome)
        self.valor=val_hora
        self.trabalhada=hora_trab

    def calc_sal(self):
        self.salario_bruto= self.trabalhada * self.valor
        self.desc= (self.salario_bruto* self.inss)/100
        self.salario= self.salario_bruto - self.desc
        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome,sal_bruto):
        super().__init__(nome)
        self.salario_bruto=sal_bruto

    def calc_sal(self):
        self.desc= (self.salario_bruto* self.inss)/100
        self.salario= self.salario_bruto - self.desc
        return self.salario

f0=Horista('paulo',12,200)
f0.calc_sal()
f0.analisar_sal()

f1=Mensalista('elton',9500)
f1.calc_sal()
f1.analisar_sal()

'''


class conta_bancaria:
    '''
        Fazer um conta bancaria e depois realizar saques e depositos 
    '''

    def __init__(self, titular, conta, saldo=0):
        self._nome = titular
        self.conta = conta
        self.__saldo = saldo
        print(f' conta criada com sucesso saldo atual é de ${self.__saldo}')

    def __str__(self):
        return f'Estado atual da conta {self.__dict__}'
    # f'nome:{self.nome}\nnumero da conta:{self.conta}\nsaldo atual:${self.saldo:.2f}'

    def deposito(self, valor):
        valor=abs(valor)
        self.__saldo += valor
        print(f'deposito de ${valor:.2f} autorizado da conta {self.conta}')

    def sacar(self, saque):
        saque=abs(saque)

        if saque <= self.__saldo:
            self.__saldo -= saque
            print(f'saque de ${saque:.2f} autorizado da conta {self.conta}')
        else:
            print('saldo insuficiente')
