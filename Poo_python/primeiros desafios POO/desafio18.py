from rich import print
from rich.panel import Panel
class churrasco:
    cunsumo_padrao:float=400
    preco_da_carne:float= 82.40

    def __init__(self,titulo,pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
   
    def quantidade_carne(self)->float:
        return self.pessoas * churrasco.cunsumo_padrao
   
    def Total_a_recadar(self)->float:
        return self.quantidade_carne() * churrasco.preco_da_carne
  
    def divisao_cada_pessoa(self)->float:
        return self.Total_a_recadar() / self.pessoas
   
    def analisar(self):
        conteudo= f'Analisando [green] {self.titulo}[/] com [blue]{self.pessoas} amigos[/]'
        conteudo += f'\nCada participante comera em media {churrasco.cunsumo_padrao}g e o kg de carne custa {churrasco.preco_da_carne} $'
        conteudo += f'\nRecomendo compra [blue] {self.quantidade_carne()}[/]'
        conteudo += f'\nCusto total será de [green] R${self.Total_a_recadar():,.2f} [/]'
        conteudo +=f'\nCada pessoa pagará [yellow] R${self.divisao_cada_pessoa():,.2f} [/] para participar.'
        print(Panel(f'{conteudo}',title=self.titulo))


c1=churrasco('churrasco de amigos',3)
(c1.analisar())

