from escola import *
from rich import inspect
def main():
    al=Aluno('elton',2011,'ADS')
    print(al.__dict__)
    print(al.idade)
    al.nascimento=2010
    al.add_curso('med')
    
    inspect(al,methods=True,private=True)

if __name__=='__main__':
    main()