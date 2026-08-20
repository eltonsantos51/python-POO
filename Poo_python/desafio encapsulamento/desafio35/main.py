from conta_bancarias_senha import ContaBancaria
from rich import inspect

def main():
    print('criando conta [BANCO ESS]')
    id=int(input('Digite o id: '))
    nome=str(input('Digiteo nome do cliente:'))
    saldo=float(input('Digite o saldo que deseja iniciar:'))
    conta=ContaBancaria(id,nome,saldo)
    conta.depositar(1000)
    conta.sacar(500)
    #conta.nome='selma'
    print(conta)
    inspect(conta, methods=True,private=True)
    
    
if __name__ =='__main__':
    main()