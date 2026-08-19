from rich import print
import time

class livro:
    def __init__(self,nome_livro,Paginas_livro):
        self.nome= nome_livro
        self.pagina= Paginas_livro
        self.pagina_atual=1
        print(f'[blue] Você acabou de abrir o livro [red] "{self.nome}"[/] '
              f'que tem [green]"{self.pagina}"[/] paginas no total.'
                f'Agora vc esta na [yellow] pagina  {self.pagina_atual}[/] [/] ')
            
    
    def avancar_pagina(self,avancar=1):
        cont=0
        for pg in range(0,avancar,1):
            if not self.fim_livro():
                self.pagina_atual += 1
                time.sleep(0.3)
                print(f'Pag{self.pagina_atual} :reverse_button: ',end='')
                cont= cont + 1                
        print(f'  Você avançou {cont} Paginas. Agora esta na [red]pagina  {self.pagina_atual}[/]')
        if self.fim_livro():
            print(f'[red] Voce chegou ao final do livro [blue] {self.nome}.[/][/]')
    
    def fim_livro(self)-> bool:
        if self.pagina_atual== self.pagina:
            return True
        else:
            return False

livro_1= livro('god of war',20)

livro_1.avancar_pagina(5)
livro_1.avancar_pagina(4)
livro_1.avancar_pagina(20)



        