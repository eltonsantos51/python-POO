from ex29 import Avaliacao
from rich import inspect,print


def main():
    a1=Avaliacao('elton','protugues')
    a1.set_nota(-9.6)
    print(f'O aluno {a1.nome} tirou {a1.get_nota()}')
    


if __name__=='__main__':
    main()