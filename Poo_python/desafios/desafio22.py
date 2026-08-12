from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int=1
    canal_max:int=5
    vol_min:int= 1
    vol_max:int=5

    def __init__(self, canal=1, volume=1):
        self.canal_atual=canal
        self.volume_atual=volume
        self.ligar_tv: bool= False
    
    def ligar_desligar(self):
        self.ligar_tv = not self.ligar_tv
    
    def canal_mais(self):
        if self.ligar_tv:
            if self.canal_atual== ControleRemoto.canal_max:
                self.canal_atual= ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    
    def canal_menos(self):
        if self.ligar_tv:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1
    
    def volume_mais (self):
        if self.ligar_tv:
            if self.volume_atual != ControleRemoto.vol_max:
                self.volume_atual += 1
    def volume_menos(self):
        if self.ligar_tv:
            if self.volume_atual != ControleRemoto.vol_min:
                self.volume_atual -= 1

    def motrar_tv(self):
        conteudo=''
        if not self.ligar_tv:
            conteudo = f':prohibited: [red]A TV está desligada.[/]' 
        else:
            conteudo= f'CANAL='
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1 ):
                if canal == self.canal_atual:
                    conteudo += f'[yellow on yellow]{canal}[/]'
                else:
                    conteudo+=f'{canal}'
            
            conteudo += f'\n VOLUME='
            for volume in range(ControleRemoto.vol_min,ControleRemoto.vol_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'
        tv= Panel(conteudo, title='[TV]', width=30)
        print(tv) 
c=ControleRemoto()
while True:
    c.motrar_tv()
    comando=str(input(f'<CH{c.canal_atual}> - VOL{c.volume_atual} + '))
    match comando:
        case '0':
            break
        case '@':
            c.ligar_desligar()
        case '<':
            c.canal_menos()
        case '>':
            c.canal_mais()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print('\n'*10)  








