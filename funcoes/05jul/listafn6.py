def bissexto(ano: int):
    if (ano%4==0 and ano%100!=0) or (ano%4==0 and ano%100==0 and ano%400==0):
        return True
    else:
        return False

###algoritmo principal
##deixei comentado porque estou importanto a função no ex7

#ano= int(input("Informe o ano: "))
#print(bissexto(ano))  #vai exibir True ou False