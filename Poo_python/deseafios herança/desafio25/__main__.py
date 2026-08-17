from rich import print
from rich.table import Table
from transporte import *

def main():
    #1
    dist=80
    entrega=Caminhao(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()} ')
    '''
    #2
    entrega_m=Moto(dist)
    entrega_d=Drone(dist)
    
    table= Table(title='Tabela de Fretes')
    table.add_column('Distancia', justify='right', style='cyan', no_wrap= True)
    table.add_column('Tipo', justify='right', style='cyan', no_wrap= True)
    table.add_column('Frete', justify='right', style='cyan', no_wrap= True)

    table.add_row(f'{dist}km',f'{type(entrega_c).__name__}',f'{entrega_c.calc_frete()}')
    table.add_row(f'{dist}km',f'{type(entrega_m).__name__}',f'{entrega_m.calc_frete()}')
    table.add_row(f'{dist}km',f'{type(entrega_d).__name__}',f'{entrega_d.calc_frete()}')

    console = Console()
    console.print(table)
 '''
    '''
    #3
    
    dist=80
    entrega=[Moto(dist),Drone(dist),Caminhao(dist)]
    
    table=Table(title='Tabela de Frete')
    
    table.add_column('Distancia')
    table.add_column('Tipo')
    table.add_column('Frete')
    
    for item in entrega:
        table.add_row(f'{dist}km',f'{type(item).__name__}',f'{item.calc_frete()}')

    print(table)
    '''   
if __name__=='__main__':
    main()