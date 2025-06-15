def obterNumInt(label: str):
    while True:
        entrada = str(input(label))
        try:
            num = int(entrada)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor "{entrada}" não é um número inteiro')


def obterNumReal(label: str):
    while True:
        entrada = str(input(label))
        try:
            num = float(entrada)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor "{entrada}" não é um número real')


def validarLimiteMin(num: int, limiteMin: int, label: str):
    while num < limiteMin:
        print(f'O número deve ser maior ou igual a {limiteMin}')
        num = obterNumInt(label)
    return num

