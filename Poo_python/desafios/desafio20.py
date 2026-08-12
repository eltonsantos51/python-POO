from rich import print
from rich.panel import Panel

class gamer:
    def __init__(self,nome,nick_name):
        self.nome=nome
        self.nick=nick_name
        self.lista_jogos=[]
    
    def add_favorito(self,*jogos):
        for jogo in jogos:
            self.lista_jogos.append(jogo)
            self.lista_jogos= sorted( self.lista_jogos, key= str.lower)
        self.formtar= '\n🎮'.join(self.lista_jogos)    
    
    def mensangem(self):
        conteudo=f'Nome real: {self.nome}'
        conteudo += f'\nJogos favoritos'
        conteudo +=f'\n [blue] 🎮{self.formtar} [/]'
        print(Panel(f'{conteudo}',title=f'jogador <{self.nick}>',width=35))


jogador=gamer('elton','vapo')
jogador.add_favorito('god of war')
jogador.add_favorito('prnice of persa')
jogador.add_favorito('ned for spid ')
jogador.add_favorito('bomba patch')
jogador.add_favorito('pess')
jogador.add_favorito('mtx')
(jogador.mensangem())

jogador_1= gamer('danila','forrte')

jogador_1.add_favorito('tiro')
jogador_1.add_favorito('roblox')
(jogador_1.mensangem())

