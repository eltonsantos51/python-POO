class Retangulo:
    def __init__(self,base=1,altura=1):
        self.__base=None
        self.__altura= None
        self.__area=None

        self.base=base
        self.altura=altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,valor):
        if not isinstance (valor, float) and not isinstance(valor, int):
            raise ValueError('Valor da base invalida')
        elif valor < 0:
            raise ValueError('O valor da base invalido')
        else:
            self.__base= valor
    
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura (self,valor):
        if not isinstance (valor, float) and not isinstance(valor, int):
            raise ValueError('Valor da altura invalida')
        elif valor < 0:
            raise ValueError('O valor da altura invalido')
        else:
            self.__altura= valor

    @property
    def area (self):
        self.__area= self.__base * self.__altura
        return self.__area 

    @area.setter
    def area(self):
        raise SyntaxError('A area nõa pode conter parametro')

    @property
    def medidas(self):
        return f'Base={self.base}\nAltura={self.altura}\nArea={self.area}'

    @medidas.setter
    def medidas(self,valores=tuple):
        if not isinstance (valores, tuple):
            raise ValueError('Por favor digite valores apena dentro de uma tupla tupla')
        if  isinstance  (valores [0], float) or isinstance(valores [0],int):
            self.base=valores[0]
        else:
            raise SyntaxError('Valor da altura invalida')
        if  isinstance  (valores [1], float) or  isinstance(valores [1],int):
            self.altura= valores[1]
        else:
           raise SyntaxError('Valor da altura invalida')
        
        if len(valores) !=2:
            raise ValueError('Por favor digite apenas dois algarismos')


    
   
    
        

        
    
       



