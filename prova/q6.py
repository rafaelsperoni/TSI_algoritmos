a = int(input("ang 1"))
b = int(input("ang 2"))
c = int(input("ang 3"))

#a soma dos 3 angulos da 180


# if a==90 or b==90 or c==90:
#     print("retangulo")

# if a>90 or b>90 or c>90:
#     print("obtusangulo")

# if a<90 and b<90 and c<90:
#     print("acutangulo")

if a==90 or b==90 or c==90:
    print("retangulo")
elif a>90 or b>90 or c>90:
    print ("obtusangulo")
else:
    print ("acutangulo")