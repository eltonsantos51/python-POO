from ex30 import Avaliacao
from rich import inspect,print


def main():
    a1=Avaliacao('elton','protugues')
    a1.nota_set=9.6
    print(f'O aluno {a1.nome} tirou {a1.nota_get} na {a1.disciplina}')
    
if __name__=='__main__':
    main()