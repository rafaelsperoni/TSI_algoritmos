'''
João comprou um saco de ração, com peso
em quilos. Ele possui dois cachorros, para
os quais fornece a quantidade de ração
em gramas. A quantidade diária de ração  
fornecida para cada cachorro é sempre a 
mesma (200g por cao por dia). Faça um 
programa que receba o peso do saco de ração
e a quantidade de ração fornecida para cada 
cachorro, calcule e mostre quanto restará de
ração no saco após 5 dias de consumo. 
'''

diaria = 200
cachorros = 2
dias = 5

saco = int(input("Informe o peso: "))

consumo = diaria * 2 * dias
resta = saco - consumo

print("Resta ", resta)

