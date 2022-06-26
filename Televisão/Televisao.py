class televisao:
    def __init__(self, canais, volume,statusVolume):
        self.canais = canais
        self.volume = volume
        self.statusVolume = True
        
    def mudo(self):
        self.statusVolume = False
        self.volume = 0;
        print("Volume Mudo")
        
    def aumentarVolume(self,numero):##RECEBE UM INTEIRO E MODIFICA O VOLUME
        if(numero<0):
            return False
        else:
            self.volume += numero
            
    def mudarCanal(self,canal):
        self.canal += canal
        
    def retorno(self):#RETORNAR AS INFORMAÇÕES DA CLASSE
        print("O canal Selecionado foi {0} e o volume atual e de {1}".format(self.canais,self.volume))
        
    