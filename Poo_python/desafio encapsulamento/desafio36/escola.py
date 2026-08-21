from abc import ABC
from datetime import date


class Pessoa (ABC):
    def __init__(self,nome:str,nasci:int):
        self._nome=nome
        self._nascimento=None
        self.nascimento=nasci    
        
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self,nasci):
        data_atual=date.today().year
        
        if nasci > data_atual or nasci < 1946:
            self._nascimento=None
            raise ValueError(f'Ano de {nasci} invalido')
        else:
            self._nascimento=nasci

    @property
    def idade(self):
        data_atua= date.today().year
        return data_atua - self.nascimento

    @idade.setter
    def idade(self,idade:int=None):
        if idade != None:
            raise PermissionError('Voce não pode mudar a idade. Mude o ano de nascimento')

class Aluno (Pessoa):
    cursos_ofciais:list=['ADS','ADM','ENG','CONT']
    def __init__(self, nome:str, nasci:int,curso:str):
        super().__init__(nome, nasci)
        self._curso=None
        self.curso=curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,es_curso:str):
        if es_curso.upper() not in Aluno.cursos_ofciais:
            raise ValueError(f'O curso {es_curso} não esta na lista de curso oficiais ')
        else:
            self._curso=es_curso

    def add_curso(self,curso:str):
        curso=curso.upper().strip()
        if len(curso) <3 or len (curso)>5:
            raise ValueError('Nome do curso deve conter de 3 a 5 letras')
        elif curso in Aluno.cursos_ofciais:
            raise NameError(f'Ja existe curso de {curso}')
        else:
            Aluno.cursos_ofciais.append(curso)

            
            
            
          
         
        

        
        

    
        
        

        

        






        

   





