'''
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
● para homens: (72.7 * h) – 58;
● para mulheres: (62.1 * h) – 44.7. 
onde h é a altura em metros.
'''


h = float(input("Informe a altura: "))
sexo = input("Informe o sexo: ")

if sexo == 'M':
    peso = (72.7 * h) - 58
    saudacao = "Amigo"
else:
    peso = (62.1 * h) - 44.7
    saudacao = "Amiga"

print(saudacao, " , Seu peso ideal: ", peso)



