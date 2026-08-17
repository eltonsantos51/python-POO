class Termostato:
    def __init__(self,tem=24):
        self.__temperatura_priv= tem
    @property

    def temperatura(self):
        return self.__temperatura_priv
    
    @temperatura.setter

    def temperatura(self,tem):
        if tem <16:
            self.__temperatura_priv= 16
        elif tem >30:
            self.__temperatura_priv=30
        else:
            if tem %0.5==0:
                self.__temperatura_priv=tem
            else:
                raise ValueError(f'A tempertura de {tem}°C é invalida!')


    @property
    def ftempertaura(self):
        return f'{self.__temperatura_priv}°C'
    
