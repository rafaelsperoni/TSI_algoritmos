a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C:"))

maior = a
menor = a

if b>maior:
    maior = b
if b<menor:
    menor = b
if c>maior:
    maior = c
if c<menor:
    menor = c

print(maior)
print(menor)