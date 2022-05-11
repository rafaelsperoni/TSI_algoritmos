#Faça um algoritmo que leia três valores inteiros distintos e informe qual o maior valor lido.

a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

#se a é o maior
if a>b and a>c :
    print("A maior")
else:
    if b>a and b>c :
        print("B maior")
    else:
        if c>a and c>b :
            print("C maior")
        else:
            print("Não achei nenhum maior")
