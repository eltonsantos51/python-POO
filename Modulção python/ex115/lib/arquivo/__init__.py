from lib.interface import *
def encontraArquivo(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close
    except:
        print('ERRO ao criar arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRDAS')
        print(a.read())


def acrescentarArquivo(nome):
    try:
        cabecalho('NOVO PESSOA')
        nome_pessoa=input('Nome: ')
        idade=int(input('idade: '))
        a=open(nome,'a')
        a.write(f'{nome_pessoa}\t{idade} anos\n')
        a.close()
    except:
        print('ERRO ao cadastra pessoa')
    else:
        print(f'Novo registro de {nome_pessoa} adicionado.')
        
