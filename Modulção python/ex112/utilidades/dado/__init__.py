def leiaDinheiro(txt):
    
    while True :
        preco= str(input(txt).replace(',','.' ))
        try:
            return float(preco)
            
        except ValueError:
            print(f'ERRO!{preco} É um  preço invalido!! ')
            
    




    
        
    
   
    
    


