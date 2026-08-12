def metade(num,formato=False):
    res= num /2
    return res if formato is False else moeda(res)

def dobro(num):
    res = num * 2
    return f'R${res:.2f}'.replace('.',',')

def aumentar(num,porc,formato=False):
    res= num +((num*porc)/100) 
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir (num,porc):
    res= num -((num*porc)/100)
    return f'R${res:.2f}'.replace('.',',')


def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')