from Televisao import * 


if __name__ == "__main__":
    print("Bem vindo a TV Juristec+")
    print("Selecione o canal desejado");
    canalSelecao = int(input(""));
    print("Selecione o volume");
    volumeSelecao = int(input(""));
    select1 = televisao(canalSelecao, volumeSelecao,True);
    ##INSTANCIANDO O OBJETO SELECT1 DA CLASSE TELEVISAO
    
    print(select1.retorno())
    
    print("Gostaria de Mudar o Canal");
    muteEscolhaCanal = input("Sim Não?");
    
    if(muteEscolhaCanal.upper()=="SIM"):
        canalADD = int(input("Canal"));
        select1.mudarCanal(canalADD);
    else:
        print(select1.retorno())
        
    print("Gostaria de Mutar o volume");
    muteEscolha = input("Sim Não?");
    
    if(muteEscolha.upper()=="SIM"):
        select1.mudo();
        print(select1.retorno())
    else:
        print(select1.retorno())
