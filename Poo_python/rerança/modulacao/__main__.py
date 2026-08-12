
from rich import print, inspect

from aluno import Aluno
from professor import Professor
from funcionario import Funcionaria

def main():
    p1= Aluno('elton',30,'ads','T001')
    p1.aniversario()
    p1.fazer_matricula()

    pr=Professor('gustavo',40,'TI','Mestrado')
    pr.aniversario()
    pr.dar_aula()

    fun= Funcionaria('danila', 28, 'secretaria','administrativo')
    fun.aniversario
    fun.bater_ponto()
if __name__=='__main__':
    main()

