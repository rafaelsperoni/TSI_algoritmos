
########entradas
def entradas():
    global n1
    global n2
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))


########calculos
def calculos(x, y):
    soma  = x + y
    media = soma / 2
    return media



########situacao
def situacao(med):
    if med >= 7.0:
        return "Aprovado"
    else:
        return "reprovado"


entradas()
media = calculos(n1, n2)
print(media)
sit_aluno = situacao(media)
print(sit_aluno)