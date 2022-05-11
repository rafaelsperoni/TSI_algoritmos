'''
ler 3 valores inteiros
encontrar o maior e o
menor
'''
a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))




#se a é o maior
if a>b and a>c :
    print("A maior ", a)
    # se o menor é o B ou C
    if b<c :
        print("B é menor", b)
    else:
        print ("C é menor", c)

else:
    if b>a and b>c :
        print("B maior")
        # se o menor é o A ou C
        if a<c :
            print("A menor")
        else:
            print("C menor")
    else:
        if c>a and c>b :
            print("C maior")
            # se o menor é o A ou B
            if a<b :
                print("A menor")
            else:
                print("B menor")
