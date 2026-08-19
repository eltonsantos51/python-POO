from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome_produto,preco=0):
        self.nome=nome_produto
        self.preco=preco
    def etiqueta (self):
        conteudo=f'{self.nome.center(30,'-')} '
        conteudo += f'{'-'*30}'
        preco_formatado=f'{self.preco:,.2f}'
        conteudo += f'{preco_formatado.center(30,'-')}'
        etiqueta=Panel(f'{conteudo}',title='Produto',width=34)
        print(etiqueta)

       
    
p1= Produto('cumputador', 1500 )

p2 = Produto('celular', 2000 )

p1.etiqueta()

        