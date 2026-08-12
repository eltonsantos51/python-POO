from pessoa import Pessoa
class Funcionaria(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo= cargo
        self.setor=setor

    def bater_ponto(self):
        print(f' O(A) funcionario(a) {self.nome} acabou de bater o ponto!')