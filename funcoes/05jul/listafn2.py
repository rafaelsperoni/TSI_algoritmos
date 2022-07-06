#funcao desenvolvida na questão 1
def primo(x: int):
    divisivel = 0 #contador das vezes q é divisivel
    #percorrer de um até x, testando se é divisível.
    for i in range(1, x+1):
        if x%i==0 : #é divisivel
            divisivel=divisivel+1

    if divisivel==2:
        return True
    else:
        return False


def quantPrimos(quant: int):
    i=0 #contador que vai de 1 em 1
    contPrimos = 0 #contador de numeros primos
    while contPrimos<quant:
        if primo(i):  #se i for primo, exibe e conta mais 1
            print(i, " é primo")
            contPrimos = contPrimos+1
        i = i+1

######## ALGORITMO PRINCIPAL
n = int(input("Informe quantos primos quer encontrar: "))
quantPrimos(n)  #executa a funcao que exibe os primos