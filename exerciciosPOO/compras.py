'''Desafio Integrador: Projeto Prático7. Sistema de Carrinho de ComprasCrie as 
classes Item (nome e preço), Carrinho e Pedido.
O Carrinho deve ter uma lista de itens e métodos para adicionar/remover.
O Pedido deve receber um Carrinho, aplicar um cupom de 
desconto se houver, e gerar a nota fiscal.'''

class Item:
    def __init__(self,nome,valor):
        self.nome=nome
        self.valor=valor

class Carrinho:
    def __init__(self):
        self.lista_carrinho=[]

    def add_carrinho(self,produto):
        self.produto=produto
        self.lista_carrinho.append(produto)
        print(f'{self.produto.nome} adicionado no carrinho.')

    def remover_carrinho(self,remover_produto):
        if remover_produto in self.lista_carrinho:
            self.lista_carrinho.remove(remover_produto)
            print(f'{remover_produto.nome} foi removido do carrinho')
        elif remover_produto not in self.lista_carrinho:
            print(f'{remover_produto.nome} não estar no carrinho')

class Pedido:

    def __init__(self,carrinho,cupom=None):
        self.carrinho=carrinho
        self.cupom=cupom

    def nota_fiscal(self):
        total=0

        print('NOTA FISCAL')

        for item in self.carrinho.lista_carrinho:
            print(f"{item.nome}: R$ {item.valor:.2f}")
            total= item.valor + item.valor
        print(f'Subtotal: {total:.2f}')

        if self.cupom == 'VALE10':
            desconto = total * 0.10
            total= total - desconto

            print(f"Desconto (Cupom VALE10): -R$ {desconto:.2f}")
        
        print(f"Total a Pagar: R$ {total:.2f}")
        print("-------------------\n")



produto_1=Item('arroz',5.00)
produto_2=Item('cafe',10.00)
produto_3=Item('feijão',7.50)
produto_4=Item('cola cola',15.00)

carrinho= Carrinho()
carrinho.add_carrinho(produto_1)
carrinho.add_carrinho(produto_2)
carrinho.add_carrinho(produto_3)

carrinho.remover_carrinho(produto_2)

novo_pedido=Pedido(carrinho)
novo_pedido.nota_fiscal()


        







       
        
        














    
    
    



            



        






