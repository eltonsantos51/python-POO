class Avaliacao:
    def __init__(self,nome,disciplina,nota=0):
        self.nome=nome
        self.disciplina=disciplina
        self._nota= nota

    #Criando atributo validavel
    @property
    def nota_get(self): #metodo getter
        return self._nota
    
    @nota_get.setter
    def nota_set(self,valor):#metodo setter
        if valor >=0 and valor <=10:
            self._nota=valor
        else:
            print('nota invalida!')

   
