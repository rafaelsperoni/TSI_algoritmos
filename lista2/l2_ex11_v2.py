a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

maior = a
menor = a

if b > maior :
    maior = b
elif b < menor :
    menor = b

if c > maior :
    maior = c
elif c < menor:
    menor = c

print ("Maior: ", maior)
print ("Menor: ", menor)

