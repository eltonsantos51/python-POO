import moeda_108
p=float(input('digite o preço: R$ '))

print(f'A metade de {moeda_108.moeda(p)} é {moeda_108.moeda(moeda_108.metade(p))}')
print(f'O dobro de {moeda_108.moeda(p)} é {moeda_108.moeda(moeda_108.dobro(p))}')
print(f'Aumentando 10%, temos {moeda_108.moeda(moeda_108.aumentar(p,10))}')
print(f'Diminuindo 13%, temos {moeda_108.moeda(moeda_108.diminuir(p,13))}')


