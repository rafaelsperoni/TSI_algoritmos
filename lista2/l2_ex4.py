#Faça um algoritmo que leia três valores inteiros distintos e informe qual o maior valor lido.

a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

menor = a

if a < menor:
    menor = a

if b < menor:
    menor = b

if c < menor:
    menor = c

print("menor valor: ", menor)