
#IMPORTANTE!! Nesta função o valor de entrada é 
# a QUANTIDADE DE NÚMEROS QUE SERÃO LIDOS
def mediaValores(quantValores: int):
    soma = 0
    for i in range(quantValores):
        x = float(input("Informe o "+str(i+1)+" número: "))
        soma = soma + x
    
    media = soma/quantValores
    return media

############ algoritmo principal
n = int(input("Informe a quantidade de números que deseja informar: "))

print(mediaValores(n))