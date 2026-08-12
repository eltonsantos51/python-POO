'''Nível Intermediário: Encapsulamento e Métodos3. Simulador de Conta BancáriaCrie a classe ContaBancaria
com atributo privado __saldo.Implemente
 os métodos depositar e sacar.O método sacar deve impedir a operação se não houver saldo suficiente.
'''

class ContaBancaria:
    def __init__(self,nome,numero,saldo):
        self.nome=nome
        self.numero_conta=numero
        self.saldo_conta= saldo
        print('Conta Cadastrada')
        self.detalhe()
      
    def detalhe(self):    
        conteudo = f'Nome:{self.nome} \n'
        conteudo += f'Numero da Conta: {self.numero_conta}\n'
        conteudo += f'Saldo da Conta:R${self.saldo_conta}'
        print(f'{conteudo}\n')
        

    def deposito_conta(self,deposito):
        
        self.saldo_conta= self.saldo_conta + deposito
        dep=f'Deposito de {deposito} realizado com sucesso. \n'
        dep+=f'Saldo atualizado: R${self.saldo_conta}\n'
        print(dep)
        
    def saque_conta(self,saque):
          
        if saque <= self.saldo_conta:
            self.saldo_conta= self.saldo_conta- saque
            print(f'Saque de {saque} realizado com sucesso.\nSaldo atualizado:{self.saldo_conta}\n')         
        else:
           print('saldo insuficiente')

conta_1= ContaBancaria('Elton',240415,5000)

conta_1.deposito_conta(5000)
conta_1.saque_conta(7000)
conta_1.saque_conta(400)

