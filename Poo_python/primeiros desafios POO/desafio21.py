from rich import print
class Caneta:
    
    def __init__(self,cor_caneta):
        self.cor= cor_caneta             
        self.caneta_destampada=True 
    def escrever(self,escrever_caneta):
        self.escrever=escrever_caneta   
    
    def destampar(self):
        self.caneta_destampada=True  
    def tampar(self):
        self.caneta_destampada=False
    
    def quebra_de_linha(self, numero=1):
        print('\n'* numero, end='')          
    
    def mensagem(self):         
        if self.caneta_destampada:    
            if self.cor =='verde':                    
                print(f' [green] {self.escrever}[/]',end='')
            if self.cor =='vermelho':
                print(f'[red] {self.escrever}[/]',end='')
            if self.cor =='azul':
                 print(f'[blue] {self.escrever}[/]',end='')
        else:
            print(f' A  caneta {self.cor}  esta tampada',end='')    
c1=Caneta('verde')
c2=Caneta('vermelho')
c3=Caneta('azul')


c2.destampar()
c3.destampar()

c1.escrever('ola meu nome é elton')
c2.escrever('quero comer')
c3.escrever('hoje tem')

(c1.mensagem())
c1.quebra_de_linha(2)
(c2.mensagem())
c2.quebra_de_linha(5)
(c3.mensagem())


        
        