

def obterNumReal(label: str):
    while True:
        num = input(label)
        try:
            num = float(num)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número real')



def obterNumRealPositivo(label: str):
    num = obterNumReal(label)

    while num <= 0:
        print(f'Entrada inválida!\nO valor inserido deve ser um número real positivo')
        num = obterNumReal(label)

    return num     
