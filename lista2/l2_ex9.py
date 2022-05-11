preco = float(input("Informe o valor do produto: "))
cond_pag = int(input("Informe a condição de pagamento: "))

if cond_pag==1 :
    desc = preco*0.15
    total = preco - desc
elif cond_pag==2 :
    desc = preco * 0.1
    total = preco - desc
elif cond_pag==3 :
    total = preco
else : 
    acr = preco * 0.1
    total = preco + acr

print("O valor pago: ", total)