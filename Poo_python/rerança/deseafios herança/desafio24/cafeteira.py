from abc import ABC, abstractmethod

class BebidaQuente(ABC):
            
    def preparar(self):
        print('--- Iniciando preparo ---')
        self.ferver= self.ferver_agua()
        self.fazer_mistura= self.mistura()
        self.servir_se= self.servir()
        print('--- Bebida pronta ---')
        print('\n'*7)
    
    def ferver_agua(self):
        print('1. Ferver agua a 100 graus celcios')
            
    @abstractmethod
    def mistura(self):
        pass
        
    @abstractmethod
    def servir(self):
        pass
    
class Cafe(BebidaQuente):
    
    def mistura(self):
        print('2. Passando agua pressurizada pelo pó de café moído.')
    
    def servir(self):
        print('3. Servindo em xicara pequena.')
   
class Cha(BebidaQuente):

    def mistura(self):
        print('3. Mergulhar o sachê de erva na agua.')
    
    def servir(self):
        print('4. Servindo na caneca de porcelana com limão')
        

class Leite(BebidaQuente):

    def mistura(self):
        print('3. Passando vapor presurizado pelo bico com leite.')
    
    def servir(self):
        print('4. Servindo na cenca grande ja com café.')


