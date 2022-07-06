#######FUNCAO
#recebe um número e verifica se é primo
#retorna um valor lógico (True or False)
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


#######ALGORITMO PRINCIPAL
num = int(input("Informe o número a verificar: "))

if( primo(num)  ): #chamada da funcao que verifica
    print(num, " é primo")
else:
    print(num, " não é primo")