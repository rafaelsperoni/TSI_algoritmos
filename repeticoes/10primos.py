#x é número a testar se é primo
num = 1
primos = 0  #contador de numeros primos encontrados
while primos<10 :

    #para cada novo valor de x, testo se x é primo
    cont = 1
    zeros = 0
    while cont <= num:
        if num%cont == 0:
            zeros=zeros+1
        cont = cont + 1

    if zeros==2:
        print(num, " é primo")
        primos = primos + 1


    ########
    num = num+1
