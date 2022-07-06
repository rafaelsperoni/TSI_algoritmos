#usar a funcao da questao 6
from listafn6 import bissexto

def diasMes(mes: int, ano: int):
    if mes>0 and mes<13:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            return 31
        elif mes==4 or mes==6 or mes==9 or mes==11:
            return 30
        elif mes==2:
            if bissexto(ano):
                return 29
            else:
                return 28

####algoritmo principal
##deixei comentado porque estou importando a funcao no exercicio 8

# m = int(input("informe o mês: "))
# a = int(input("informe o ano: "))

# print("O mês tem ", diasMes(m, a), " dias.")
