'''
Escreva um programa que leia as medidas dos    lados de um triângulo    e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:            (valor 2.0)
− Triângulo Equilátero: possui os 3 lados iguais.    
− Triângulo Isóscele: possui 2 lados iguais.    
− Triângulo Escaleno:    possui 3 lados diferentes.
'''
a = int(input("lado 1"))
b = int(input("lado 2"))
c = int(input("lado 3"))

# if a == b and a == c:
#     print("Equilátero")

# if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
#     print("isoscele")

# if a!=b and a!=c and b!=c:
#     print ("Escaleno")


# if a == b and a == c:
#     print("Equilátero")
# elif a==b or a==c or b==c:
#     print("isoscele")
# else:
#     print ("Escaleno")


if a!=b and a!=c and b!=c:
    print("escaleno")
else:
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print("isóscele")
    else: 
        print("equilatero")