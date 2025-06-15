#início - 24/05 12:10
#fim    - 24/05 12:38

def obterNumInt(label: str):
    while True:
        num = input(label)
        try:
            num = int(num)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número inteiro')


def obterNumInteiroPositivo(label: str):
    num = obterNumInt(label)

    while num <= 0:
        print(f'Entrada inválida!\nO valor inserido deve ser um número inteiro positivo')
        num = obterNumInt(label)

    return num     


def obterNumInteiroNegativo(label: str):
    num = obterNumInt(label)

    while num >= 0:
        print(f'Entrada inválida!\nO valor inserido deve ser um número inteiro negativo')
        num = obterNumInt(label)

    return num  


def obterNumInteiroLimiteMin(label: str, limiteMin: int):
    num = obterNumInt(label)

    while num < limiteMin:
        print(f'Entrada inválida\nO número inserido deve ser maior ou igual a {limiteMin}')
        num = obterNumInt(label)

    return num


def obterNumInteiroLimiteMax(label: str, limiteMax: int):
    num = obterNumInt(label)

    while num > limiteMax:
        print(f'Entrada inválida\nO número inserido deve ser menor ou igual a {limiteMax}')
        num = obterNumInt(label)

    return num


def obterNumInteiroNaFaixa(label: str, limiteMin: int, limiteMax: int):
    num = obterNumInt(label)

    while num < limiteMin or num > limiteMax:
        print(f'Entrada inválida\nO número inserido deve estar entre {limiteMin} e {limiteMax}')
        num = obterNumInt(label)

    return num


