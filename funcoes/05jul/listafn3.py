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


#Agora, a função quer encontrar os numeros primos até N
# o que muda é a variável que determina a parada da repetição
def primosAteN(limite: int):
    i=0 #contador que vai de 1 em 1
    while i<=limite:
        if primo(i):  #se i for primo, exibe e conta mais 1
            print(i, " é primo")
        i = i+1

######## ALGORITMO PRINCIPAL
n = int(input("Informe o limite: "))
primosAteN(n)  #executa a funcao que exibe os primos