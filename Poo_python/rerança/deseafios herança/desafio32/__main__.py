from diario import*
from rich import inspect,print


def main():
    d1=Diario()
    d1.escrever('meu nome é elton ')
    d1.escrever('estou estudando')
    d1.escrever('gosto de futebol')
    try:
        d1.ler('teste')
    except Exception as e:
        print(f'[red] ERRO! {e}[/]')


if __name__=='__main__':
    main()