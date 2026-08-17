from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade= idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso=curso
        self.turma= turma
    
    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer sua matricula! ')

    def estudar(self):
        print(f' aluno {self.nome} esta estudando {self.curso} na turma {self.turma}')

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade= especialidade
        self.nivel=nivel

    def dar_aula(self):
        print(f'O professor {self.nome} acabou de dá aula!')

    def estudar(self):
        print(f'o professor {self.nome} é especialista  {self.especialidade} no nivel {self.nivel} ')

class Funcionaria(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo= cargo
        self.setor=setor

    def bater_ponto(self):
        print(f' O(A) funcionario(a) {self.nome} acabou de bater o ponto!')

    def estudar(self):
        print(f'{self.nome} esta estudadndo para {self.cargo} do setor de {self.setor}')