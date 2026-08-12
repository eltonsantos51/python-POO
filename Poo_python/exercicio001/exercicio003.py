
class conta_bancaria:
    '''
        Fazer um conta bancaria e depois realizar saques e depositos 
    '''
    def __init__(self,titular,conta, saldo=0):
        self.nome= titular
        self.conta=conta
        self.saldo=saldo
        print(f' conta criada com sucesso saldo atual é de ${self.saldo}')
    def __str__(self):
        return f'nome:{self.nome}\nnumero da conta:{self.conta}\nsaldo atual:${self.saldo:.2f}'
    def deposito(self,valor):
        self.saldo +=  valor
        print(f'deposito de ${valor:.2f} autorizado da conta {self.conta}')

    def sacar(self,saque):
        
        if saque <= self.saldo:
            self.saldo -=  saque
            print(f'saque de ${saque:.2f} autorizado da conta {self.conta}')
        else:
            print('saldo insuficiente')

cliente_1= conta_bancaria('elton',9210,5000)
cliente_1.deposito(50)
cliente_1.sacar(100000)

print(cliente_1)


