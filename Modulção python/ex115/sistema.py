from lib.interface import *
from lib.arquivo import *
from time import sleep

arq='cadastro de pessoas.txt'
if not encontraArquivo(arq):
    criararquivo(arq)
 
while True:
   
    resposta=painel(['Ver Pessoa cadastrada','Cadastrar Pessos','Sair do sistema'])
    
    if resposta ==1:
        lerArquivo(arq)
    elif resposta==2:
        acrescentarArquivo(arq)
    elif resposta==3:
        cabecalho('Finalizando processo... Volte sempre!')
        break
    else:
        print('[red] ERRO: Digite uma opção valida[/]')
    sleep(2)
  


    

