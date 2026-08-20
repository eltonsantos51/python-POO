from hashlib import sha256
import pwinput
class ContaBancaria:
    def __init__(self,id:int, nome:str, saldo:float=0, senha:str=None):
        self._id=id
        self._titular=nome
        self.__saldo=saldo
        if senha is None:
            senha= self.pedi_senha()
        self.__hash=sha256(senha.encode()).hexdigest()
        self.nome=nome
        print(f'Conta {id} criada com sucesso.Saldo total de {self.__saldo:.2f}')

    @property
    def nome(self):
        return self._titular
    @nome.setter
    def nome(self, nome:str):
        
        if type(nome)== str and nome.replace(" ",'').isalpha():
            self._titular=nome 
        else:
            raise ValueError('Por favor digite o nome do usuario')

    def pedi_senha(self):
        while True:
            senha=pwinput.pwinput(prompt='Criar senha:')
            if len(senha) >=6:
                break
        return senha

    def depositar(self,depositar:float=0):
        self.deposito=abs(depositar)
        self.__saldo= self.__saldo + self.deposito
        print(f'Deposito de {self.deposito:.2f} na conta {self._id}')
        

    def sacar(self,saque:float=0,senha:str=None):
        self.saque=abs(saque)
        dsenha=senha
        if senha is None:
            dsenha=pwinput.pwinput(prompt='senha:')
            validar=sha256(dsenha.encode()).hexdigest()
            if validar==self.__hash:
                self.__saldo= self.__saldo - self.saque
                print(f'Saque de {self.saque:.2f} autorizado na conta {self._id} ')

            else: 
                print('senha incorreta')
        else:
            validar=sha256(dsenha.encode()).hexdigest()
            if validar==self.__hash:
                self.__saldo= self.__saldo - self.saque
                print(f'Saque de {self.saque:.2f} autorizado na conta {self._id} ')
            else:
                print('senha incorreta')
    def __str__(self):
            return f'A conta {self._id} de {self.nome} tem {self.__saldo} de saldo'
    
    
  
        

        



        

        

            


        

    
        

        


    

    
        
        

    
    
        
    
