from batalha import *

def main():
    p1=Guerreiro('Kratos',2000)
    
    p2=Mago('Merlin',3000)
    
    p1.atacar(p2,2000)
    p2.cura()

if __name__=='__main__':
    main()