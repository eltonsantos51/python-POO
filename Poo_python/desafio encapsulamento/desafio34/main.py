from retangulo import Retangulo
def main ():
    r=Retangulo()
    try:
        r.base=6
        r.altura=10
        #r.medidas=(5,3)
        print(r.medidas)
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}:{e}')
    

if __name__ =='__main__':
    main()