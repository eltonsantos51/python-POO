class Porta:
    def abrir(self):
        print('puxar maçaneta e empurrar')
class Empresa:
    def abrir(self):
        print('entrar no portal do empreendedor em abrir um cnpj')
class Ovo:
    def abrir(self):
        print('quebra o ov usando uma colher')

class Pedra:
        pass
#solução usando dock typer
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'tivemos uma problema ao abrir{objeto.__class__.__name__}')