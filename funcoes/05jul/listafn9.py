#para esta questão, utilizaremos uma informação importante:
#no Python, podemos percorrer uma string por seus indices
# se  s = "Rafael",    a primeira posição (índice 0) é a letra R
#portanto s[0] vale "R", s[1] vale "a", s[2] vale "f" ...
def verificaCPF(cpf: str):
    #primeiro digito verificador
    soma = 0
    for i in range(9):
        peso = 10-i
        soma = soma + int(cpf[i])*peso
    resto = soma % 11
    if resto<2:
        dv1 = "0"
    else:
        dv1 = 11-resto

    #segundo digito verificador
    soma = 0
    for i in range(10):
        peso = 11-i
        soma = soma + int(cpf[i])*peso
    
    resto = soma % 11
    if resto < 2:
        dv2 = "0"
    else:
        dv2 = 11-resto

    if dv1==int(cpf[9]) and dv2==int(cpf[10]):
        return True
    else:
        return False

##algoritmo principal

print(verificaCPF('94136912072') )