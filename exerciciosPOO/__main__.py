
from  aluno import *

def main():
    aluno_1=Aluno('elton', 174563, 9.5, 5.4, 7.0)
    aluno_1.nome_aluno()
    aluno_1.media()
    aluno_1.aprovado()

    aluno_2=Aluno('Danila', 455122, 9.0, 6.4, 8.0)
    aluno_2.nome_aluno()
    aluno_2.media()
    aluno_2.aprovado()
     
    aluno_3=Aluno('Daila', 969010, 3.0, 5.0, 6.0)
    aluno_3.nome_aluno()
    aluno_3.media()
    aluno_3.aprovado()

    aluno_4=Aluno('Selma', 451839, 10.0, 8.5, 7.5)
    aluno_4.nome_aluno()
    aluno_4.media()
    aluno_4.aprovado()

    aluno_5=Aluno('Elivelton', 427518, 4.5, 5.4, 9.0)
    aluno_5.nome_aluno()
    aluno_5.media()
    aluno_5.aprovado()
    print('\n')

    turma = [aluno_1,aluno_2,aluno_3,aluno_4,aluno_5]
    melhor_aluno = max(turma, key=lambda aluno: aluno.media())
    print(f"O aluno com a maior média é {melhor_aluno.nome} com média {melhor_aluno.media_nota:.1f}")

    Pior_aluno = min(turma, key=lambda aluno: aluno.media())
    print(f"O aluno com a menor média é {Pior_aluno.nome} com média {Pior_aluno.media_nota:.1f}")
        
           
if __name__=='__main__':
    main()