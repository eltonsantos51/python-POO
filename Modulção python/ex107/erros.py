try:
    n1=int(input('primeiro numero: '))
    n2=int(input('segundo numero: '))
    res=n1/n2
except(ValueError,TypeError):
    print('tivemos um problema com tipo de dados que vc digitou')
except ZeroDivisionError:
    print('impossivel dividir qualquer numero por 0')
except KeyboardInterrupt:
    print('o usuario preferiu não informar dados')
except Exception as erro:
    print(f'O erro que foi encontrado foi {erro.__cause__}')
else:
    print(f'O  valor da divisão foi {res:.2f}')
finally:
    print('Programa encerrado, vote sempre!!')