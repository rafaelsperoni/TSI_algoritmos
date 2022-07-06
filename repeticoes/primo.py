x = 1
while x<=100:
    y = 1
    zeros = 0  #conta as vezes q deu resto 0
    while y <= x:
    #        print (x, "%", y, " resulta ", x%y)
        if x%y == 0 : #se resto for zero
    #            print (x, " por ", y , "deu resto 0")
            zeros = zeros + 1

        y = y+1

    if (zeros == 2):  # se a qtdade de restos 0 ==2
        print (x, " primo")
    else:
        print(x, " nao primo")

    x = x+1