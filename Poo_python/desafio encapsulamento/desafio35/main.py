from conta_bancarias_senha import ContaBancaria
from rich import inspect

def main():
    conta=ContaBancaria(658,'elton santos',5654,)
    conta.depositar(1000)
    conta.sacar(500)
    
    print(conta)
    
    
    

    
if __name__ =='__main__':
    main()