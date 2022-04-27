'''
#  Uma padaria vende uma certa quantidade de
#  pães franceses e uma quantidade de broas
#  a cada dia. Cada pão custa R$ 0,50 e a
#  broa custa R$ 1,50. Ao final do dia, o
#  dono quer saber quanto arrecadou com a
#  venda dos pães e broas (juntos), e quanto 
#  deve guardar numa conta de poupança 
# (10% do total arrecadado). Faça um algoritmo 
# para ler as quantidades de pães e de broas, 
# e depois calcular os dados solicitados.
'''
paes = float(input("Informe quantos pães: "))
broas = float(input("Informe quantas broas: "))

preco_pao = 0.5
preco_broa = 1.5

#calcula quanto arrecadou em paes
total_paes = paes*preco_pao
#quanto arrecadou em broas
total_broas = broas*preco_broa

#arrecadacao total (paes e broas)
total = total_paes + total_broas

#10% d valor total é p poupança
poupanca = total*0.1

print("O total arrecadado: R$ ", total)
print("Guardar na poupança: R$ ", poupanca)