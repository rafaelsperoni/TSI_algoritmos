#usando as funcoes dos exercicios 6 e 7
from listafn7 import diasMes

def verificaData(dia: int, mes: int, ano: int):
    
    if dia>0 and dia<=diasMes(mes, ano):
        return True
    else:
        return False

###algoritmo principal - Testando datas de 2024, que é bissexto
print(verificaData(31, 1, 2024))
print(verificaData(32, 1, 2024))
print(verificaData(28, 2, 2024))
print(verificaData(29, 2, 2024))
print(verificaData(30, 4, 2024))
print(verificaData(31, 4, 2024))
