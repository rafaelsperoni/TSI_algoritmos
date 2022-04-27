n1 = float(input("Informe nota 1: "))
n2 = float(input("Informe nota 2: "))
n3 = float(input("Informe nota 3: "))

freq = float(input("Informe o percentual de frequência: "))

media = (n1+n2+n3)/3

if (media>=7.0) and (freq>=75.0):
  print("Aprovado")
else:
  if (freq>=75):
      exame = float(input("Informe nota do exame: "))
      final = (media + exame)/2
      if final>=5:
          print("Aprovado com exame. Média ", final)
      else:
          print("Reprovado no exame. Média ", final)
  else:
      print("Reprovado por frequencia")