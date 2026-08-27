from abc import ABC,abstractmethod
class Arquivo (ABC):
    def __init__(self,nome:str,tamanho:float):
        self.nome=nome
        self._extensao='' 
        self.tamanho= tamanho
        self.nome_completo=''
    @abstractmethod
    def abrir(self):
        pass


class Doc(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self.calc= tamanho / 1000000
        self._extensao='docx'
        self.nome_completo=f"'{nome}.{self._extensao}'({self.calc:.2f} MB)"

    def abrir(self):
        return print(f'Abrir arquivo {self.nome_completo} no Micrisoft Word')

class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self.calc= tamanho / 1000000
        self._extensao="pdf"
        self.nome_completo=f'"{nome}.{self._extensao}"({self.calc:.2f} MB)'

    def abrir(self):
        return print(f'Abrir arquivo {self.nome_completo} no Adobe Reader')


def abrir_arquivo(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Não foi possivel encontrar o {objeto.__class__.__name__}')
    
