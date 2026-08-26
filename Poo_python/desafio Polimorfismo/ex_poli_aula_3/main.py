from ex_03 import*
def main():
    c1=Carteira(100)
    c2=Carteira(100)
    ##c1 -= 10
    if (c1==c2):
        print('os valores são iguais')
    else:
        print('as carteiras tem valores diferentes')

    if (c1 <= c2):
        print('A seginda carteira tem mais dinheiro')
    else:
        print('A primeira carteira tem mais dinheiro')

    print(c1)
    print(c2)

   
    


if __name__=='__main__':
    main()