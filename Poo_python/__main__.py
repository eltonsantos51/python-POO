from rich import print, inspect
from classexercicio005 import Aluno, Professor, Funcionaria

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

    p1.estudar()
    pr.estudar()
    fun.estudar()

if __name__=='__main__':
    main()

#inspect(p1, methods= True)
#inspect(pr,methods= True)
#inspect(fun, methods= True)


    