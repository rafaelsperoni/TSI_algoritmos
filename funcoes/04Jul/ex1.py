#Faça um algoritmo contendo uma sub-rotina que retorne
# 1 se o número digitado for positivo ou zero. 
# Retorne 0 se o número for negativo.

from funcoes import *

a = int(input("Informe o valor"))
y = positNeg(a)
if y==0:
    print("negativo")
else:
    print("zero ou positivo")


if verificaCPF("11111111111"):
    print("valido")