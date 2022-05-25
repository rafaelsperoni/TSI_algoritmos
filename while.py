cont=0

mediaTurma = 0.0
somatorio = 0.0

while cont <5 :
    print("Aluno ", cont)
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))

    media = (n1 + n2)/2

    print ("a média: ",media)

    somatorio = somatorio + media #acumula

    cont = cont + 1 #incremento

mediaTurma = somatorio / cont

print(mediaTurma)