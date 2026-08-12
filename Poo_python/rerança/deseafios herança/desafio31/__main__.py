from termostato import Termostato
from rich import inspect

def main():
    t1=Termostato()
    try:
        t1.temperatura=10.5
    except Exception as e:
        print(f'houve um problema: {e} ')
    print(f'A temperatura atual é {t1.ftempertaura}')


    #inspect(t1, private=True, methods= True)
    
if __name__== '__main__':
    main()