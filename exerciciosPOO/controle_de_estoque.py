''' Controle de Estoque Crie uma classe Produto com nome, preco e quantidade.
Crie métodos para adicionar_estoque e vender_produto.
A venda deve atualizar a quantidade e retornar o valor total pago.'''

class ControleEstoque:
    def __init__(self,nome,preco,quantidade):
        
        self.nome= nome
        self.preco=preco
        self.quantidade= quantidade
        print('produto cadastado')
        produto=f'Nome:{self.nome}\n'
        produto +=f'Preço: R${self.preco:.2f}\n'
        produto +=f'Estoque:{self.quantidade}\n'
        print(produto)
        print('')

    def add_estoque(self,numero_mercadoria=0):
        
        
        self.numero_merc= numero_mercadoria
       
        if numero_mercadoria >0:
            self.quantidade = self.quantidade + self.numero_merc
            print(f'{self.nome}:{self.quantidade} \nEstoque atualizado!')
            print('')
        else:
            print('operação invalida')
            print('')

    def vender_estoque(self,venda):
        
        self.soma_venda=0
        self.quantidade_venda=venda
        
        
        if self.quantidade_venda <= self.quantidade:
            self.soma_venda= self.preco* self.quantidade_venda
            self.quantidade= self.quantidade - self.quantidade_venda
            conteudo=f'O produto {self.nome} vendido com sucesso!\n'
            conteudo += f'Foi comprado {self.quantidade_venda}.\n'
            conteudo +=f'Valor total da venda foi R${self.soma_venda:.2f}\n'
            conteudo+=f'Estoque atualizado: {self.quantidade}'
            print(conteudo)
            return self.soma_venda
        else:
            print('estoque insuficionete')


loja_1=ControleEstoque('fazer250',21000,10)
loja_1.add_estoque(5)
loja_1.vender_estoque(6)



