matr = input("Informe sua matricula:")
p1 = float(input("Informe nota prova 1:"))
p2 = float(input("Informe nota prova 2:"))
p3 = float(input("Informe nota prova 3:"))
trab = float(input("Informe nota trabalhos:"))

peso1 = 1.0
peso2 = 2.0
peso3 = 2.0
peso4 = 1.0

media = (p1*peso1 + p2*peso2 + p3*peso3 + trab * peso4) / 6
print(media)

if media>=9:
    conceito = "A"
elif media>=7.5 :
    conceito = "B"
elif media>=6.0 :
    conceito = "C"
elif media>=4 :
    conceito = "D"
else :
    conceito = "E"

print("Estudante ", matr, "tem média ", media, ", e conceito ", conceito)

if conceito == "A" or conceito == "B" or conceito == "C" :
    print("Aprovado") 
else:
    print("Reprovado")