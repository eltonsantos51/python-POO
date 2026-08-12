class Item:
    # 1. O Item só guarda o nome e o preço de UM produto por vez
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    # 2. O Carrinho nasce com uma lista de itens totalmente vazia
    def __init__(self):
        self.itens = []

    # Método para adicionar o objeto Item na lista
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item.nome} adicionado ao carrinho.")

    # Método para remover o item da lista
    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item.nome} removido do carrinho.")
        else:
            print(f"{item.nome} não está no carrinho.")


class Pedido:
    # 3. O Pedido recebe o Carrinho e um cupom opcional (que começa como None)
    def __init__(self, carrinho, cupom=None):
        self.carrinho = carrinho
        self.cupom = cupom

    # Gera a nota fiscal calculando o total e aplicando o desconto
    def gerar_nota_fiscal(self):
        total = 0
        
        print("\n--- NOTA FISCAL ---")
        # Soma o preço de cada item que está dentro do carrinho
        for item in self.carrinho.itens:
            print(f"{item.nome}: R$ {item.preco:.2f}")
            total += item.preco
        
        print(f"Subtotal: R$ {total:.2f}")

        # Aplica o cupom de desconto se ele existir (ex: 'VALE10' dá 10% de desconto)
        if self.cupom == "VALE10":
            desconto = total * 0.10
            total -= desconto
            print(f"Desconto (Cupom VALE10): -R$ {desconto:.2f}")
        
        print(f"Total a Pagar: R$ {total:.2f}")
        print("-------------------\n")


# === TESTANDO O SISTEMA COMPLETO ===

# Passo 1: Criamos os itens individuais
arroz = Item("Arroz", 4.50)
feijao = Item("Feijão", 6.45)
leite = Item("Leite", 5.00)

# Passo 2: Criamos o carrinho e adicionamos os itens nele
meu_carrinho = Carrinho()
meu_carrinho.adicionar_item(arroz)
meu_carrinho.adicionar_item(feijao)
meu_carrinho.adicionar_item(leite)

# Passo 3: Criamos o pedido passando o carrinho e o cupom de desconto
novo_pedido = Pedido(meu_carrinho, cupom="VALE10")

# Passo 4: Geramos a nota fiscal final
novo_pedido.gerar_nota_fiscal()
