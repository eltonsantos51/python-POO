from rich import print
def leiaInt(txt):
    while True:
        try:
            inteiro=int(input(txt))
            return int(inteiro)
        except (ValueError,TypeError):
            print('[red]ERRO! Digite um valor inteiro valido!![/]')
        except KeyboardInterrupt:
            print('ERRO! Nenhum valor foi digitado, por padrão o valor sera 0')
            return 0
        

def leiaFloat(txt):
    while True:
        try:
            real=float(input(txt))
            return float(real)
        except (ValueError,TypeError):
            print('[red]ERRO! Digite um valor real valido!![/]')
        except KeyboardInterrupt:
            print('ERRO! Nenhum valor foi digitado, por padrão o valor sera 0 ')
            return 0



