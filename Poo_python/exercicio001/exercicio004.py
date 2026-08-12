from rich import print , inspect
class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade= idade

    def aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso=curso
        self.turma= turma
    
    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer sua matricula! ')

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade= especialidade
        self.nivel=nivel

    def dar_aula(self):
        print(f'O professor {self.nome} acabou de dá aula!')


class Funcionaria(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo= cargo
        self.setor=setor

    def bater_ponto(self):
        print(f' O(A) funcionario(a) {self.nome} acabou de bater o ponto!')


p1= Aluno('elton',30,'ads','T001')
p1.aniversario()
p1.fazer_matricula()

pr=Professor('gustavo',40,'TI','Mestrado')
pr.aniversario()
pr.dar_aula()

fun= Funcionaria('danila', 28, 'secretaria','administrativo')
fun.aniversario
fun.bater_ponto()


inspect(p1, methods= True)
inspect(pr,methods= True)
inspect(fun, methods= True)


    