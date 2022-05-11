#Encontrar o dobro de um número inteiro 
# informado caso ele seja positivo e o
#  seu triplo caso seja negativo, 
# imprimindo o resultado. 

a = int(input("Informe A: "))

if a>=0: 
    res = a*2

if a<0 :
    res = a*3

print(res)