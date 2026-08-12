'''
menor_peso=0
maior_peso=0

for pes in range(1,6):
    peso=float(input(f'Peso da {pes}º pessoa: '))
    if pes ==1:
        maior_peso=peso
        menor_peso=peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        
        if peso > maior_peso:
            maior_peso=peso

print(f' o maior peso digitado foi {maior_peso}kg')
print(f'O menor peso digitado foi {menor_peso}kg')

'''

'''
media_idade=0
soma=0
homem_velho=0
nome_homem=''
tot_20=0
for pes in range(1,5):
    print(5*'-=',f'{pes}º Pessoa',5*'=-')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('sexo[M/F]: ')).upper()
    soma= soma + idade
  
    if sexo == 'M':
        if idade>homem_velho:
            homem_velho=idade
            nome_homem=nome
    if sexo=='F':
        if idade<20:
            tot_20= tot_20 + 1
                
media_idade= soma/4
print(f'A media de idade do grupo é de {media_idade} anos')
print(f'Homen mais velho tem {homem_velho} anos e se chama {nome_homem}')
print(f'Ao todo foram {tot_20} mulheres com menos de 20 anos.')
'''


''' 
sexo=str(input('Informe seu sexo:')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo=str(input('Opção invalida, Por favor informe seu sexo:')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
'''
'''
from random import randint
print('sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue advinhar?')

resultado= randint(0,10)
palpite=None
tentativas=0
while palpite != resultado:
    palpite=int(input('Qual seu palpite? '))
    tentativas += 1
    if palpite < resultado: 
        print('Mais..Tente mais uma vez..')
    elif palpite > resultado:
        print('Menos... Tente mais uma vez..')
    elif palpite == resultado:
        print(f'Acertou com {tentativas} tentativas.... parabens! ')
'''

'''
from time import sleep
numero_1= int(input('Primeiro valor: '))
numero_2= int(input('Segundo valor: '))
op= None
while op !='5':
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Numeros\n'
          '[5] Sair do Programa')
    op=str(input('>>>>> Qual é a sua opção? '))
    if op =='1':
        print(f'A soma de {numero_1} com numero {numero_2} é {numero_1 + numero_2}')
    elif op == '2':
        print(f'A mutiplicação entre {numero_1} e {numero_2} é { numero_1 * numero_2}')
    elif op == '3':
        if numero_1 > numero_2:
            print( f'{numero_1} é maior que {numero_2}.')
        elif numero_1 < numero_2:
            print(f'{numero_1} é menor que {numero_2} ')
        else:
            print('Os dois numeros são iguais!!')
    elif op == '4':
        print('informe os numeros novamente!')
        numero_1= int(input('Primeiro valor: '))
        numero_2= int(input('Segundo valor: '))
    elif op=='5':
        print('Finalizando ')
    else:
        print('Opção invalida. tente novamento!')
    print(10*'-=')
    sleep(2)
print('Fim de programa, volte sempre!')
'''
'''
numero=int(input('Digite um numero: '))
fatorial=1
print(f'Calculando {numero}!=',end=' ')
while numero > 1:
    print(numero, end=' x ')
    fatorial= fatorial * numero
    numero= numero - 1 
print(f'1 ={fatorial}')
'''
'''
numero= int(input('digte um numero: '))
fatorial=1
print(f'fatorial de {numero}!=',end='')
for num in range(numero,0,-1):
    fatorial= fatorial*num 
    print(num,end='')
    print(' x ' if num > 1 else' =',end='')

print(fatorial)
    
'''
'''       
primeiro= int(input('primeiro termo: '))       
razao=int(input('Razão: '))

termo= primeiro
contador=1

while contador <= 10:
    print(termo,end='->')
    termo=termo+ razao

    contador= contador + 1

print('fim')
'''
'''
print('Gerador de PA')
print(5*('-='))
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão PA:'))
cont=1
termo=primeiro
op=10
while op!=0:
    cont=1
    while cont <= op:
        print(termo,end='->')
        termo= termo + razao
        cont= cont + 1
    print('pausa')
    op=int(input('Quantos termos voce quer mostrar mais? ')) 
    '''
'''     
print(20*"-=")
print('Sequencia de fibonacci')
print(20*'=-')
termo= int(input('Quantos termos voce quer mostrar? '))
cont=0
t1=0
t2=1

print(f'{t1}-> {t2}',end='-> ')
while cont <=termo-3:
    t3= t1+t2
    print(t3,end='-> ')
    t1=t2
    t2=t3
    cont=cont + 1
print('fim')
'''
'''
c=0
soma=0
numero=None
while numero != 999:
    numero=int(input('digite um numero [999 para parar]: '))
    if numero!=999:
        c= c + 1 
        soma = soma + numero

print(f'Voce digitou {c} numeros e a soma entre eles foi {soma }')
'''
'''
op=None
cont=media=soma=maior_numero=menor_numero=0

while op !='N':
    numero=int(input('Digite um numero: '))
    op=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    cont+=1
    soma+=numero
    if cont==1:
        maior_numero=numero
        menor_numero=numero
    else:
        if numero>maior_numero:
            maior_numero=numero
        if numero < menor_numero:
            menor_numero=numero

media=soma/cont
print(f'Voce digitou {cont} numero e a media entres eles foi {media:.2f}')
print(f'O maior valor foi {maior_numero} e o menor valor foi {menor_numero}')
'''
'''
cont=0
soma=0
while True:
    numero=int(input('digite um numero: '))
    if numero==999:
        break
    cont=cont +1
    soma=soma + numero

print(f' A soma dos {cont} numeros foi {soma}.')
'''
'''
while True:
    tabuada=int(input('quer ver tabuada de qual valor: '))
    print('-='*20)
    for tab in range(1,11):
        res= tab* tabuada
        print(f'{tabuada} x {tab} = {res}')
    print('-='*20)
    if tabuada < 0:
        break
'''

'''
from random import randint
print(20*'-=')
print('Vamos jogar Par ou Impar')
print(20*'-=') 

vitoria=0
while True:
    jogador=int(input('Diga um valor: '))
    computador= randint(0,10)
    resultado= jogador + computador
    escolha=''
    while escolha != 'P' and escolha != 'I' :
        escolha=str(input('escolha Impar ou Par: [I/P]')).upper().strip()[0]
    print(f'Voce jogou {jogador} o cumputadro jogou {computador}. Total de {resultado} ',end='')
    print('DEU PAR'if resultado % 2 ==0 else  "DEU IMPAR" )
    if escolha=='P':
        if resultado%2==0:
            print('Voce VENCEU')
            vitoria+=1
        else:
            print('Voce PERDEU')
            break
    elif escolha == 'I':
        if resultado%2==1:
            print('Voce VENCEU')
            vitoria+=1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Voce venceu {vitoria} vezes')
    
'''
'''
pessoas18 = homens = mulheres20 = 0
while True:
    print(20*'-=')
    print('Cadastre uma Pessoa ')
    print('-='*20)
    idade=int(input('Idade: '))
    sexo=''
    while sexo != 'F' and sexo !='M':
        sexo= str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >=18:
        pessoas18 +=1
    
    if sexo == 'M':
        homens+=1
    
    if sexo =='M':
        if idade <20:
            mulheres20+=1
    desejo=''
    while desejo != 'S' and desejo !='N':
        desejo=str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if desejo=='S':
        continue
    elif desejo=='N':
        break

print(f'Total de pessoas com mas de 18 anos: {pessoas18}')    
print(f'Ao todo temos {homens} homen cadastrados.')
print(f'Temos {mulheres20} mulher com menos de 20 anos.')
    
'''
'''

print('=-'*20)
print('SUPERMERCADO BARATÃO')
print('-='*20)
total_compra= compra_1000= menor_preco= cont =  0
nome_produto=''
while True:
    produto=str(input('Nome do produto: ')).strip()
    preco=float(input('Preço:R$  '))   
    cont= cont +1
    total_compra= total_compra + preco
    if preco > 1000:
        compra_1000= compra_1000 + 1
    
    if cont ==1:
        menor_preco=preco
        nome_produto=produto
    else:
        if preco < menor_preco:
            menor_preco=preco
            nome_produto=produto
    
    desejo=''
    while desejo != 'S' and desejo != 'N':
        desejo= str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if desejo=='S':
        continue
    elif desejo=='N':
        break

print(f'Fim do programa')

print(f'O total de compras foi: {total_compra}')
print(f'Temos {compra_1000} produto que custa mais de R$ 1.000 ')
print(f'O produto mais barato foi {nome_produto} e custou {menor_preco}')
'''
'''
print('='*20)
print('BANCO CEV')
print('='*20)
saque= int(input('Que valor voce quer sacar?R$ '))
nota_50=50
nota_20=20
nota_10=10
nota_1=1
resto=saque
if resto>=nota_50:
    nota_50= resto // 50
    resto= resto % 50
    print(f'total de {nota_50} cédulas de R$50 ')  
if resto >=nota_20:
    nota_20= resto // 20
    resto=resto % 20
    print(f'Total de {nota_20} cédulas de R$20 ')  
if resto >=nota_10:
    nota_10= resto//10
    resto=resto % 10
    print(f'Total do {nota_10} cedulas de R$10')   
if resto >=nota_1:
    nota_1= resto//1
    resto= resto%1
    print(f'Total de {nota_1} cedulas de R$1')
print('=-'*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

'''

'''
print('='*20)
print('BANCO CEV')
print('='*20)
valor= int(input('quanto vc quer sacar:R$ '))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total = total - ced
        totced= totced + 1
    else:
        if totced>0:
            print(f' Total de {totced} cedulas de R${ced}')
        
        if ced == 50:
            ced=20
        
        elif ced==20:
            ced=10
        
        elif ced==10:
            ced=1
        totced=0
        
        if total==0:
            break
print('=-'*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

'''
'''
numeros=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nome','dez',
         'onze', 'doze','treze','qautorze','quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')
while True:
    escolha = int(input('escolha um numero entre 0 e 20:'))
    if escolha>=0 and escolha <=20:
        break
print(f'Voce digitou o numero {numeros[escolha]}')
'''
'''
times=("Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Red Bull Bragantino", 
       "Bahia", "Coritiba", "São Paulo", "Atlético-MG", "Corinthians", "Cruzeiro", 
       "Botafogo", "Vitória", "Internacional", "Santos", "Grêmio", "Vasco", "Remo", 
       "Mirassol", "Chapecoense")

print(20*'-=')
print(f'Listas dos times do brasilierão: {times}')
print(20*'-=')
print(f'Os 5 primeiros são: {times[:5]}')
print(20*'-=')
print(f'Os 4 ultimo0s são: {times[16:]}')
print(20*'-=')
print(f'Times em ordem alfabetica :{sorted(times)}')
print(20*'-=')
print(f'Chapecoense esta na {times.index('Chapecoense')+1}º posição.')
'''
'''
from random import randint
numeros=[]
for num in range(5):
    numeros.append(randint(1,9))
numeros=tuple(numeros)
print(f'Os numeros sorteados forma {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor  sorteado foi {min(numeros)}')
'''
'''
from random import randint

numeros=(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
print('Os numeros sorteados fora: ',end='')
for num in numeros:
    print(num,end=' ')
   
print('')
print(f'o maior numero foi {max(numeros)}')
print(f'O menor numeros foi {min(numeros)}')

'''
'''
n1=int(input( 'digte um numero: '))
n2=int(input('digie mais um numero: '))
n3=int(input('digie outro numero: '))
n4=int(input('digite um ultimo numero: '))

numeros=(n1,n2,n3,n4)
print(f'Voce digitou os valores{numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O numero 3  não digitado em nunhuma posição')
print(f'Os valores pares digitados foram',end=' ')
par=0
for num in numeros:
    if num %2==0:
        par=num
        print(num,end=' ')
        
'''
'''
lista=('lapis',1.75,
       'borracha',2.00,
        'caderno',15.90,
        'estojo',25.00,
        'tranferidor',4.20,
        'compasso',9.99,
        'mochila',120.32,
        'caneta',22.30,
        'livro',34.90,)
print('-='*20)
print(f'{'Lista de Dompras':^40}')
print('-='*20)
for pos,produto in enumerate(lista):
    
    if pos % 2==0:
        print(f'{lista[pos]:.<30}',end='')
    if pos % 2==1:
        print(f'R$  {lista[pos]:.2f}')
print('-='*20)

'''
'''
palavras = ('APRENDER', 'PROGRAMAÇAO','PYTHON','CASA','JOGAR','LINGUAGEM',
            'PRATICAR','ESTUDAR','TRABALHAR','PRATICAR')
vogal='aeiou'
for palavra in palavras:
        print(f'\nNa palavra {palavra} temos',end=' ')
        for letra in palavra.lower():
            if letra in vogal:
                  print(f'{letra}',end=' ')
                        
'''
'''
lista_numero=[]
for num in range(0,5):
    numero=int(input(f'digite um numero na posição {num}: '))
    lista_numero.append(numero)
maior= max(lista_numero)
menor= min(lista_numero)
print('-='*20)
print(f'Voce digitou os valores{lista_numero}')
print(f'O maior valor foi {maior} nas posições ',end='')
for pos, val in enumerate(lista_numero):
    if val== maior:
        print(f'{pos}...',end='') 
print('')
print(f'O menor valor foi {menor} nas posições ',end='')
for pos,val in enumerate(lista_numero):
    if val == menor:
        print(f'{pos}...',end=' ')
'''

'''  
lista_num=[]

while True:
    numero=int(input('Digite um valor: '))    
    if  numero not in lista_num:
        lista_num.append(numero)
        print('Adicionado com sucesso ')
    else:   
        print('Valor duplicado! Não vou adicionar..')
    desejo=''
    while desejo !='S' and desejo != 'N':
        desejo= str(input('deseja continuar: [S/N]')).upper().strip()[0]
    if desejo=='S':
        continue
    elif desejo =='N':
        break

lista_num.sort()
print(f'Voce digitou os valores {lista_num}')
'''
'''
lista_numero=[]

for c in range(0,5):
    numero= int(input('Digite um valor:'))
    if c==0 or numero > lista_numero[-1]:
        lista_numero.append(numero ) 
        print('Adiconado ao final da lista')
    else:
        pos=0
        while pos < len(lista_numero):
            if numero <= lista_numero[pos]:
                lista_numero.insert(pos,numero)
                break
            pos= pos +1
        print(f'Adicionado na posição {pos} da lista')
           
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista_numero}')
'''

'''
lista_numero=[]
while True:
    numero=int(input('digite um valor:'))
    lista_numero.append(numero)

    desejo=''
    while desejo != 'S' and desejo != 'N':
        desejo=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    
    if desejo=='S':
        continue
    elif desejo == 'N':
        break
print('=-'*30)
print(f'Voce digitou {len(lista_numero)} elementos.')
lista_numero.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista_numero}')
if 5 in lista_numero:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
 
'''
'''
lista_completa=[]
lista_par=[]
lista_impar=[]
while True:
    numero=int(input('Digite um numero: '))
    lista_completa.append(numero)
    if numero % 2==0:
        lista_par.append(numero)
    if numero % 2 == 1:
        lista_impar.append(numero)

    desejo=''
    while desejo!='S' and desejo != 'N':
        desejo=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if desejo=='N':
        break
print('-='*30)   
print(f'lista completa é: {lista_completa}')
print(f'lista da pares é : {lista_par}')
print(f'lista de impares é: {lista_impar}')        
'''
'''
equação=str(input('digite a expressão: '))
lista_simb=[]
for simb in equação:
    if simb=='(':
        lista_simb.append('(')
    elif simb==')':
        if len(lista_simb)>0:
            lista_simb.pop()
        else:
            lista_simb.append(')')
            break

if len(lista_simb)==0:
    print('equaçõa valida ')
    
else:
    print('equação invalida')
    

'''
'''
import datetime
consecionaria=[]
carros=[]
for c in range(0,2):
    carros.append(str(input('nome:')))
    carros.append(int(input('ano:')))
    consecionaria.append(carros[:])
    carros.clear()

ano_atual= datetime.datetime.today().year
for a in consecionaria:
    res=ano_atual - a[1]
    if res>=15:
        print(f'{a[0]} tem {res} anos de fabriçaõ, por isso é isento de IPVA')
    else:
        print(f'{a[0]} tem {res} anos de fabricação, não esta isento de IPVA')
    
'''


'''
lista_pessoas=[]
pessoa=[]
while True:
    pessoa.append(str(input('nome:')))
    pessoa.append(float(input('Peso:')))
    lista_pessoas.append(pessoa[:])
    pessoa.clear()
    desejo=''
    while desejo != 'S' and desejo!='N' :
        desejo=str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if desejo=='N':
        break
maior=0
menor=0
lista_nome_menor=[]
lista_nome_maior=[]
for pos,p in enumerate( lista_pessoas):
    if pos==0:
        maior=p[1]
        menor=p[1]
        lista_nome_menor.append(p[0])
        lista_nome_maior.append(p[0])
    else:
        if p[1] > maior:
            maior=p[1]
            lista_nome_maior.clear()
            lista_nome_maior.append(p[0])
        elif p[1]==maior:
            lista_nome_maior.append(p[0])
           
        if p[1]<menor:
            menor=p[1]
            lista_nome_menor.clear()
            lista_nome_menor.append(p[0])
        elif p[1]==menor:
            lista_nome_menor.append(p[0])
            
print(f'-='*30)
print(f'Ao todo voce cadstrou {len(lista_pessoas)} pessoas ')
print(f'O maior peso foi de {maior}kg foi de {lista_nome_maior}')
print(f'O menor peso foi de {menor}kg foi de {lista_nome_menor}')
'''


'''
lista_temp=[]
lista_def=[]
maior= 0
menor= 0
while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(float(input('Peso: ')))
    if len(lista_def) ==1:
        maior=lista_temp[1]
        menor=lista_temp[1]
    else:
        if lista_temp[1] > maior:
            maior= lista_temp[1]
        if lista_temp[1] < menor:
            menor=lista_temp[1]
    lista_def.append(lista_temp.copy())
    lista_temp.clear()
    desejo=str(input('deseja continuar?[S/N]'))
    if desejo in 'Nn':
        break
print('=-'*30)
print(f'Ao todo vc cadastrou {len(lista_def)} pessoas')
print(f'O maior peso foi {maior}kg. Peso de ',end='')
for p in lista_def:
    if p[1]==maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi {menor}kg. Peso de ', end='')
for p in lista_def:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
'''
'''
princ=[]
lista_par=[]
lista_impar=[]
for c in range(1,8):
    numero=int(input(f'digite o {c}º valor: '))   
    if numero % 2 ==0:
        lista_par.append(numero)
        lista_par.sort()       
    else:
        lista_impar.append(numero)
        lista_impar.sort()
princ.append(lista_impar.copy())
princ.append(lista_par.copy())
lista_impar.clear()
lista_par.clear()
print('-='*30)
print(f' Os valores pares digitados foram: {princ[1]}')
print(f'Os valores impares digitados foram: {princ[0]} ')
'''
'''
princ=[[],[]]

for c in range(1,8):
    numero=int(input(f'digite o {c}º valor: '))   
    if numero % 2 ==0:
        princ[1].append(numero)
       
    else:
        princ[0].append(numero)
        
princ[0].sort()
princ[1].sort()

print('-='*30)
print(f' Os valores pares digitados foram: {princ[1]}')
print(f'Os valores impares digitados foram: {princ[0]} ')
'''
'''
matriz_prin=[[],[],[]]
for p in range(0,3):
    matriz_prin[0].append(int(input(f'digite um valor:[0 , {p}]:')))
for s in range(0,3):
    matriz_prin[1].append(int(input(f'Digite um valor:[1 , {s}]:')))
for t in range(0,3):
    matriz_prin[2].append(int(input(f'Digite um valor:[2 , {t}]:')))
print('-='*20)
for res in matriz_prin:
    print(f'{res}')

    matriz=[[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int( input(f'Digite um valor:[{l} , {c}]: '))
print('=-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()

'''
'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor: [{l} , {c}] '))
print('=-'*20)
soma_par=0
soma_coluna=0
maior_valor=0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c]%2==0:
            par=matriz[l][c]
            soma_par=soma_par+par     
    print()  
for l in range(0,3):
    soma_coluna= soma_coluna+matriz[l][2]

for c in range(0,3):
    if c ==0:
        maior_valor=matriz[1][c]
    else:
        if matriz[1][c] > maior_valor:
            maior_valor=matriz[1][c]
                
print('=-'*20)
print(f'A soma de todos os numeros pares são {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')
'''
'''
import random
print('=-'*20)
print(f'JOGAR NA MEGA SENA')
print('=-'*20)
lista_mega=[]
ordem=0

quant= int(input('Quantos jogos voce quer que sorteie? '))
for s in range(0,quant):
    
    sorteio= random.sample(range(1,61),6)
    lista_mega.append(sorteio)
    lista_mega[ordem].sort()
    ordem= ordem + 1

cont=0
print(f'SORTANDO {quant} JOGOS')
for s in lista_mega:
    cont=cont+1
    print(f'Jogo {cont}: {s}')
    
'''
'''
lista_prin=[]
lista_temp=[]
while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(float(input('Nota 1: ')))
    lista_temp.append(float(input('Nota 2: ')))
    media= (lista_temp[1]+lista_temp[2]) / 2
    lista_temp.append(media)
    lista_prin.append(lista_temp.copy())
    lista_temp.clear()
    desejo=''
    while desejo != 'S' and desejo !='N':
        desejo=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if desejo=='N':
        break
print('-='*40)
print('No.  NOME       MEDIA')
print('-'*20)
for i, val in enumerate(lista_prin):
    print(f'{i}   {lista_prin[i][0]}     {lista_prin[i][3]:.1f}')     

while True :
    print('-'*20)
    opc=int(input('Mostrar nota de qual aluno? (999 interrompe)'))
    if opc <= len(lista_prin)-1:
            print(f'Notas de {lista_prin[opc][0]} são [{lista_prin[opc][1]},{lista_prin[opc][2]}]')
    if opc==999:
         break
print(5*'>','Volta sempre',5*'<')

'''
'''
estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade faderativa; '))
    estado['silga']=str(input('sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
'''

'''
aluno={}

aluno['Nome']=str(input('Nome:'))
aluno['Media']=float(input('Media: '))

if aluno['Media']>=7:
    aluno['situação']='Aprovrado'
elif aluno['Media'] < 7 and aluno['Media']>=5:
    aluno['situação']='Recuparação'
else:
    aluno['situação']='Reprovado'

for k,v in aluno.items():
    print(f'-{k} é igual a {v}')
'''
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo={}
ranking={}

for c in range(1,5):
    dado= randint(1,6)
    jogo[f'Jogador{c}']= dado
print('Valores Sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print(30*'-=')
print('== RANKING DOS JOGADORES ==')
ranking=sorted(jogo.items(),key= itemgetter(1), reverse=True)

for i , v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}.')
    sleep(1)
'''
'''
import datetime
funncionario={}
ano_atual= datetime.date.today().year
funncionario['nome']=str(input('Nome: '))
nascimento= int(input('Ano de nascimento: '))
funncionario['idade']= ano_atual - nascimento
funncionario['ctps']= int(input('Carteira de Trabalho (0 naõ tem): '))

if funncionario['ctps']!=0:
    funncionario['contratação']=int(input('Ano de contratação: '))
    tempo=funncionario['contratação']-nascimento
    funncionario['aposentadoria']= tempo + 35
    funncionario['salario']=float(input('Salario: R$'))
print(30*'-=')

for k,v in funncionario.items():
    print(f'-{k} tem o valor {v}')
'''
'''
jogador={}
gols=[]
jogador['nome']=str(input('Nome do jogador: '))
partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols']= gols
jogador['total']=sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for chave,valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print(30*'-=')
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas')
for i , g in enumerate(gols):
    print(f'=> Na partida {i}, fez {g} gols.')

print(f'Foi um total de {jogador["total"]} gols')
'''
'''
cadastro_pessoa={}
cadastro_geral=[]
soma=0
while True:
    cadastro_pessoa['nome']=str(input('Nome:'))
    cadastro_pessoa['sexo']=''
    while cadastro_pessoa['sexo'] != 'F' and cadastro_pessoa['sexo']!='M':
        cadastro_pessoa['sexo']=str(input('Sexo: [F/M]')).upper().strip()[0]
        if cadastro_pessoa['sexo'] != 'F' and cadastro_pessoa['sexo']!='M':
            print('ERRO! Por favor, digite M ou F.')
    cadastro_pessoa['idade']=int(input('Idade: '))
    cadastro_geral.append(cadastro_pessoa.copy())
    soma=soma + cadastro_pessoa['idade']
    opc=''
    while opc != 'S' and opc !='N':
        opc=str(input('Quer continuar?[S/N]')).upper().strip()[0]
        if opc!='S' and opc!='N':
            print('ERRO! Responda apenas S ou N.')
    if opc== 'N':
        break
media=soma/ len(cadastro_geral) 
print(30*'-=')
print(f'A) Ao todo temos {len(cadastro_geral)} pessoas cadastradas')
print(f'B) A media de idade é de {media:.2f} anos')
print('c) As mulheres cadastradas foram',end=' ' )
for c in cadastro_geral:
    if c['sexo']=='F':
        print(f'{c["nome"]}',end=' ')
print('')
print('D) A lista das pessoas que estão acima da media:')
for c in cadastro_geral:
    if c['idade'] > media:
        print(c)
'''
'''
jogador={}
gols_marcados=[]
time=[]
while True:
    jogador['nome']=str(input('Nome do jogador: '))
    partidas=int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    total=0
    gols_marcados.clear()
    for c in range (0,partidas):
        gol=int(input(f'    Quantos gols fez na partida {c+1}? '))
        gols_marcados.append(gol)
        total= total + gol
    jogador['gols']= gols_marcados.copy()
    jogador['total']=total
    time.append(jogador.copy()) 
    opc=''
    while opc != "S" and opc !="N":
        opc=str(input('deseja continuar? [S/N]')).upper()[0]
    if opc =='N':
        break
print(30*'-=') 
print(f'{'Cod':<3} {'Nome':<6} {'Gols':^10} {'Total':>10}')
print(20*'--')
for i, val in enumerate(time):
    str_gols=str(val['gols'])
    print(f'{i:<3} {val["nome"]:<6} {str_gols:^10} {val["total"]:>10}')
    str_gols=val['gols']

while True:
    print(20*'--')
    analisar=int(input('Mostrar dados de qual jogador? (999 parapar)'))
    for i , val in enumerate(time):
        if analisar == i:
            print(f'- LAVANTAMENTO FOI DO JOGADOR {val['nome']}:')
            for j , g in enumerate (val['gols']):
                print(f'No jogo {j} fez {g} gols.')
    if analisar> len(time) and analisar !=999:
        print(f'Não existe jogaddor {analisar}')
    if analisar==999:
        break
print('<<< Volte sempre >>>')

'''
'''
def terreno(larg,compri):
    
    res= larg * compri
    print(f'A area  de um terreno {larg:.1f}x{compri:.1f} é de {res:.1f}m².')

print('Controle de Terreno')
print('-'*20)
largura=float(input('LARGURA (m) :'))
comprimento=float(input('COMPRIMENTO (m):'))
terreno(largura,comprimento)
'''
'''
def texto(txt):
    quant= len(txt)+4
    
    print(quant*'~')
    print(f"  {txt}")
    print(quant*'~')

texto(' meu nome é elton ')
texto(' elton ')
texto(' elivelton ')
texto(' danila ')
texto('oi')
'''

'''
from time import sleep
def linha():
    print('-='*20)
def contagem (inicio,fim,passo=1):
    if passo== 0:
        passo=1
    if passo<0:
        #passo=passo * -1
        passo=abs(passo)
    print(f'Contagem  de {inicio} ate {fim} de {passo} em {passo} ')
    if inicio > fim:
        c=inicio
        while c >=fim:
            print(c,end=' ',flush=True)
            sleep(0.5)
            c=c-passo
    else:
        c=inicio
        while c <=fim:
            print(c,end=' ',flush=True)
            sleep(0.5)
            c=c+passo
    print('FIM!')
contagem(0,10,1)
contagem(10,0,2)
linha()
print('Agora é sua vez de personalizar a contagem!')
ini=int(input('Inicio: '))
fi=int(input('Fim: '))
pas=int(input('Passo: '))
contagem(ini,fi,pas)

'''
'''
from time import sleep
def maior(*num):
    print('-='*20)
    print('Analisandoo valores repassados...')
    maior_numero= cont =0
    for c in num:
        print(c, end=' ',flush=True)
        sleep(0.5)
        if cont==0:
            maior_numero=c
        else:
            if maior_numero<c:
                maior_numero=c
        cont=cont+1
    print(f'Fora informados {cont} ao todo.')
    print(f'o maior valor informado foi {maior_numero}.')
maior(2,9,4,5,7,1)
maior(7,4,0)
maior(1,2)
maior(-1,-2,-7)
maior(6)
maior()
'''
'''
from random import randint

def sorteia(lista):
   
    for num in range(0,5):
        sorteio= randint(0,9)
        sort.append(sorteio)
    print(f' Sorteando {len(sort)} valores da lista:', end=' ')
    for numero in sort:
        print(numero, end=' ')
    print('PRONTO!')
    return sort
def SomaPar(lista=list):
    soma=0
    for par in lista:
        if par % 2==0:
            soma= soma + par
    print(f'Somando os valores pares de {lista}, temos {soma} ')

sort=[]
sorteia(sort)
SomaPar(sort)
'''
'''
def contador(i,f,p):
    """ É um contadro que mostra na tela uma contagem de numeros inteiros.
    :para i: inicio da contagem
    :para f: fim da contagem
    :para p: passo da contagem

    """
    cont=i
    while cont <= f:
        print(cont,end=' ')
        cont = cont+ p
    print('Fim!')

contador(0,10,2)

help(contador)
'''
'''
def teste(b):
    global a
    b= b + 4
    c=2
    a=7
    print(f'a dentro vale{a}')
    print(f'c dentro vale {c}')
    print(f'b dentro vale {b}')
a=5
teste(a)
print(f'a fora vale {a} ')
'''

'''
def voto(ano):
    from datetime import date
    ano_atual=date.today().year
    res= ano_atual - ano
    if res < 16:
        return f'Com {res} anos: NÃO VOTA'
    elif res>=18  and res <=65:
        return f'Com {res} anos:  VOTO OBRIGATORIO'
    else:
        return f'Com {res} anos: VOTO É OPICIONAL'
print('--'*20)
nasc=int(input('Em que ano você nasceu?'))
print(voto(nasc))
'''
'''
def fatorial(numero,show=False):
    """-> calcula um fatorial de um numero:
        :para numero: O numero para ser calculado 
        :para show: (Opcional) Mostra ou não a conta.
        :para return: O valor fatorial de um numero.
    """
    fat=1
    print('-='*10)
    for f in range(numero,0,-1):
        fat= fat * f
        if show==True:
            if f >1:
                x='x'
            else:
                x='='
            print(f'{f}{x}',end='')
    return fat

print(fatorial(5,show=True))
help(fatorial)
'''

'''
def ficha(n='<desvconhecido>', g=0):
    if not n:
        n='<desvconhecido>'
    if str(g).isnumeric():
        g=int(g)
    else:
        g=0
    return f'O jogador {n} fez {g} gols(s) no campeonato'

print('-='*10)
nome=str(input('Nome do jogador: '))
gol=str(input('Numero de gols: '))
print(ficha(nome,gol))
'''
'''
def leiaint(text):
    leia=''
    numero=False
    while numero==False :
        leia=(input(text))
        if leia.isnumeric():
            leia=int(leia)
            numero=True  
        else:
            print('ERRO!, Digite um numero inteiro valido!')
            
    return leia
        
# programa principal
n=leiaint('Digite um numero:')
print(f'Voce acabou de digitar o numero {n}')
    
'''
"""

def notas(*n,sit=False):
    ''' A função analisa as notas de vario alunos.
        :para n: Uma ou mais notas de alunos (ceitavel varias).
        :para sit: A situação das medias dos alunos.(Opcional)
        :return: Um dicionario com os dados do aluno, como quantas notas, maior note, menor nota,
        e a sutiação do aluno.

    '''
    boletin={}
    boletin['nota']= n 
    maior=menor= media=tot=soma=0
    for c in boletin['nota']:
        soma=soma+c
        tot=tot+1
        if tot==1:
            maior=c
            menor=c
        else:
            if maior <c:
                maior=c
            elif menor> c :
                menor=c
    media= soma/ tot
    boletin['total']=tot
    boletin['maior']=maior
    boletin['menor']=menor
    boletin['media']=media
    del(boletin['nota'])
    if  sit:
        if boletin['media'] < 5:
            boletin['situação']='RUIM'
        elif  boletin['media']>=5 and boletin['media'] <7:
            boletin['situação']='ROZOAVEL'
        else:
            boletin['situação']='BOA'
    return boletin
aluno= notas(10.6,5.6,2.5,1,6)
print(aluno)
help(notas)

"""

