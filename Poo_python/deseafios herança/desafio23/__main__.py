from poligono import *
from rich import print,inspect

def main():
    p1= Circulo(12)

    print(f'Perimetro= {p1.perimetro():.1f}')
    print(f'Area= {p1.area():.1f}')
    inspect(p1, methods= True)
if __name__=='__main__':
    main()