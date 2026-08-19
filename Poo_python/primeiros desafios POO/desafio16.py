from rich import print
from rich  import inspect

class Funcionario:
    empresa= 'urso em video'
    def __init__(self,nome,setor,cargo):
        self.nome=nome
        self.setor=setor
        self.cargo=cargo
    def apresentação(self):
        return f':flexed_biceps_dark_skin_tone: ola meu nome é [blue] {self.nome} [/] sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'


c1=Funcionario('elton','TI','prgramador')

print(c1.apresentação())

c2=Funcionario('danila','adminstrativo','diretora')
print(c2.apresentação())
c3=Funcionario('daila','administrativo','gerente')
print(c3.apresentação())