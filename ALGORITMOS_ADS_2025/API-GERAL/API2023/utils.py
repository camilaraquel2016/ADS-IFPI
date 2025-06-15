#NÚMERO REAL - FUNÇÕES

def obterNumReal(label: str):
    while True:
        num = input(label)
        try:
            num = float(num)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor "{num}" não é um real válido')


def obterNumRealLimiteMin(label: str, limiteMin: float):
    num = obterNumReal(label)

    while num < limiteMin:
        print(f'Entrada inválida!\nO número inserido deve ser maior ou igual a {limiteMin}')
        num = obterNumReal(label)
    return num


def obterNumRealLimiteMax(label: str, limiteMax: float):
    num = obterNumReal(label)

    while num > limiteMax:
        print(f'Entrada inválida!\nO número inserido deve ser menor ou igual a {limiteMax}')
        num = obterNumReal(label)
    return num


def obterNumRealNaFaixa(label: str, limiteMin: float, limiteMax: float):
    num = obterNumReal(label)

    while num < limiteMin or num > limiteMax:
        print(f'Entrada inválida!\nO número inserido deve estar entre {limiteMin} e {limiteMax}')
        num = obterNumReal(label)
    return num


def obterNumInteiro(label: str):
    while True:
        num = input(label)
        try:
            num = int(num)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor "{num}" não é um inteiro válido')
 



def obterNumInteiroNaFaixa(label: str, limiteMin: int, limiteMax: int):
    num = obterNumInteiro(label)

    while num < limiteMin or num > limiteMax:
        print(f'Entrada inválida!\nO número inserido deve estar entre {limiteMin} e {limiteMax}')
        num = obterNumInteiro(label)
    return num




