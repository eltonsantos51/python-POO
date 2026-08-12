'''Nível 1: Classes e Atributos DinâmicosTermômetro Inteligente: Crie uma classe Termometro que guarda a 
temperatura em Celsius.Adicione propriedades (getters e setters) para que, ao ler ou definir a temperatura
em Fahrenheit, o cálculo seja feito automaticamente.

Registro de Vôo: Crie uma classe Voo com numero_voo,
destino e vagas_disponiveis. Adicione um método reservar_assento() que diminui as vagas (se houver) e 
retorna um booleano de sucesso.'''

'''
'''
class Voo:
    def __init__(self,numero_v,destino,vagas_disponiveis=0):
        self.numero_voo=numero_v
        self.destino=destino
        self.vagas= vagas_disponiveis 
        self.lista_passageiros={}

    def reservar_assento(self,nome,vagas):
        if vagas <=0:
            print('erro na quantidade')
            return False
        
        if self.vagas >= vagas:
            self.vagas= self.vagas - vagas

            if nome in self.lista_passageiros:
                self.lista_passageiros[nome] += vagas

            else:
                self.lista_passageiros[nome]= vagas
        print(f"Operação realizada com sucesso! {nome} reservou {vagas} vagas para {self.destino}.")
        print(f"Vagas restantes no voo {self.numero_voo}: {self.vagas}")
        return True
    

v1=Voo(9602,'são paulo',100)

v1.reservar_assento('elton',3)
v1.reservar_assento('danila',1)
v1.reservar_assento('selma',3)
''' 