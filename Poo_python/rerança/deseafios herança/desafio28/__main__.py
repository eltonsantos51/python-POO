
from jogos import *


def main():
    c1 = conta_bancaria('elton', 1252, 5000)
    c1.deposito(-500)
    c1.sacar(-100)
   
    print(c1)

    '''
    conta1= ContaBancaria(9690,'elton',5000)
    print(conta1)
    conta1.depositar(50)
    conta1.sacar(2000)
    '''
    '''
    c1=funcionario('Elton','TI','Programador')
    print(c1.apresentação())
    c2=funcionario('Danila','Gerente','Adminstrativo')
    print(c2.apresentação())
'''


if __name__ == '__main__':
    main()
