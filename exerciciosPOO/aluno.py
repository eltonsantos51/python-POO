
class Aluno :
    def __init__(self,nome,matricula, nota_1,nota_2,nota_3,):
        self.nome=nome
        self.numero_matricula= matricula
        self.nota_1= nota_1
        self.nota_2= nota_2
        self.nota_3= nota_3
        print()
    def nome_aluno(self):
        print(f'Nome: {self.nome}\n'
                     f'Matricula:{self.numero_matricula}')
   
    def media(self):
        self.media_nota= (self.nota_1 + self.nota_2 + self.nota_3) / 3
        return self.media_nota
    
    def aprovado(self):
        valor_media=self.media()
        print(f'Media:{self.media_nota:.1f}')
        if valor_media > 6:
            print(f'Aluno {self.nome} foi aprovado, parabens!') 
        else:
            print(f'Aluno {self.nome} reprovado!')

      




