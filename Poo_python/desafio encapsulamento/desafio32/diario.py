from rich import print
class Diario:
    def __init__(self,senha='ed@51'):
        self.__senha= senha
        self.__segredo=[]

    
    def escrever(self,escrev):
        return self.__segredo.append(escrev)
    
    def ler(self,senha=None):
        if senha == self.__senha:
            print('[green] DIARIO LEBARADO[/]' )
            for seg in self.__segredo:
                print(f'-{seg}')
        else:
            raise PermissionError('Senha invalida! Voce nã pode ler o diario.')

        

    