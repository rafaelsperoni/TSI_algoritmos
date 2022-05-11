'''
O IMC – Indice de Massa Corporal é um critério
 da Organização Mundial de Saúde para dar uma
 indicação sobre a condição de peso de uma pessoa adulta. 
 A fórmula é IMC = peso / ( altura )2

Elabore um algoritmo que leia o peso e a
 altura de um adulto e mostre sua condição
  de acordo com a tabela abaixo.

'''

h = float(input("Informe a altura: "))
peso = float(input("Informe o peso: "))

imc = peso / h**2

if imc<18.5:
    classif = "abaixo do peso"
elif imc<=25 :
    classif = "normal"
elif imc<=30 :
    classif = "acima do peso"
else :
    classif = "obeso"

print ("Você está ", classif)