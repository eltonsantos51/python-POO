from rich import print
def leiaInt(txt):
    while True:
        try:
            inteiro=int(input(txt))
            
        except (ValueError,TypeError):
            print('[red]ERRO! Digite um valor inteiro valido!![/]')
            continue
        except KeyboardInterrupt:
            print('[red]ERRO! Nenhum valor foi digitado, por padrão o valor sera 0[/]')
            return 0
        else:
            return inteiro


def linha(tam=30):
    print('-'*tam)


def cabecalho(txt):
    linha()
    print(txt.center(30))
    linha()
    
def painel(list): 
    cabecalho('MENU PRINCIPAL') 
    c=1 
    for intem in list:
        print(f'{c}-[blue]{intem}[/]')
        c=c+1
    linha()
    opc=leiaInt('Sua opção: ')
    return opc
    

       
       