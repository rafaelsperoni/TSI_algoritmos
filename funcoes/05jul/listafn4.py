def calculadora(n1: int, n2: int, operacao: str):
    if operacao=='+':
        res = n1+n2
    elif operacao=='-':
        res = n1-n2
    elif operacao == '*':
        res = n1*n2
    elif operacao == '/':
        res = n1/n2

    return res

######## algoritmo principal
a = int(input("informe o primeiro número"))
b = int(input("informe o segundo número"))
op = input("Informe a operação (+, -, * ou /")

print( calculadora(a, b, op) )