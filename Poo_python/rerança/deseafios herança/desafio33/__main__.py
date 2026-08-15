from rich import print
from senha import Credencial
def main():
    s1= Credencial()
    try:
        s1.senha='helton'
        #s1.validar('eltonsantos')
        print(s1.senha)
    except Exception as e:
        print(f'[red]ERRO!{e}[/]')
    
if __name__=='__main__':
    main()
