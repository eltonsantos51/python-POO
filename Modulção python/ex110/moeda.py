def metade(num,formato=False):
    res= num /2
    return res if formato is False else moeda(res)

def dobro(num,formato=False):
    res = num * 2
    return res if formato is False else moeda(res)
    

def aumentar(num,porc,formato=False):
    res= num +((num*porc)/100) 
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir (num,porc,formato=False):
    res= num -((num*porc)/100)
    if formato is False :
        return res
    else:
        return moeda(res)


def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0,aumento=0,reducao=0):
    print('=-'*20)
    print(f'{"RESUMO VALOR":^40}')
    print('-='*20)
    
    print(f'Preço analizado:\t{moeda(preco)}')
    print(f'Dobro do Preço:\t\t{dobro(preco,True)}')
    print(f'Metade do Preço:\t{metade(preco,True)}')
    print(f'{aumento}% de aumento:\t\t{aumentar(preco,aumento,True)}')
    print(f'{reducao}% de desconto:\t{diminuir(preco,reducao,True)}')
    print('-='*20)





