def fibo(numero):
    futuro = 0
    presente = 0
    passado = 0
    for x in range(numero+1):
        if(x==0):
            passado += 0
        if(x==1):
            presente += 1
        futuro = presente+passado
        presente = passado
        passado = futuro
        #presente = passado
        #print("presente{} \n passado{} \n futuro{}".format(presente,passado,futuro))
        print("{} {}".format(x,futuro))
        

if __name__ == '__main__':
    N = int(input())
    fibo(N)