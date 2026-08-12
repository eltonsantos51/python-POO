def metade(num):
    res= num /2
    return res

def dobro(num):
    res = num * 2
    return res

def aumentar(num,porc):
    res= num +((num*porc)/100) 
    return res


def diminuir (num,porc):
    res= num -((num*porc)/100)
    return res


def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')