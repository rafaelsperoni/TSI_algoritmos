
cont = 1
zeros = 0
num = int(input("Informe o número a verificar: "))

while cont<=num :
    resto = num % cont
    print(resto)
    if (resto == 0):
        zeros = zeros + 1
        
    cont = cont + 1

print("divisivel ", zeros, "vezes.")
if zeros == 2:
    print("primo")
else:
    print("não é primo")