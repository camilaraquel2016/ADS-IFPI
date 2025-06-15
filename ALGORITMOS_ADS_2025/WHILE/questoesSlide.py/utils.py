def obterNumInt(label: str):
    entrada = str(input(label))

    try:
        num = int(entrada)
        return num
    except ValueError:
        print(f'Entrada inválida!\nO valor "{entrada}" não é um número inteiro')
        return obterNumInt(label)


def obterNumReal(label: str):
    entrada = str(input(label))

    try:
        num = float(entrada)
        return num
    except ValueError:
        print(f'Entrada inválida!\nO valor "{entrada}" não é um número real')
        return obterNumReal(label)


