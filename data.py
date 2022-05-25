dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

diasg = dia
messg = mes
anosg = ano

if mes == 2:
    if dia == 28:
        diasg = 1
        messg = mes+1
    else:
        diasg = dia + 1

elif mes == 4 or mes == 6 or mes==9 or mes==11:
    if dia == 30:
        diasg = 1
        messg = mes+1
    else:
        diasg = dia + 1
else:

    if dia==31:
        diasg = 1
        if mes==12:
            messg = 1
            anosg = ano+1
        else:
            messg = mes+1
    else:
        diasg = dia + 1

print(diasg, "/", messg, "/", anosg)
