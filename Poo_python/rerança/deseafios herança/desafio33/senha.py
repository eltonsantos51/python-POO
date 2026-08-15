from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__senha=None

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self,chave):
        if len(chave) > 0:
            self.__senha= sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise PermissionError('Por favor digite a senha ')

    
    def validar (self,chave):
        usuario= sha256(chave.encode('utf-8')).hexdigest() 

        if usuario == self.__senha:
            print('senha correta')
            return True
        else:
            print('senha incorreta')
            return False

     
        
        





