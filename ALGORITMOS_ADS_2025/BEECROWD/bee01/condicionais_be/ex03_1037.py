def esta_no_intervalo(num):
    return num >= 0 and num <= 100


def obter_intervalo(num: float):
    if num <= 25:
        return '[0, 25]'
    elif num <= 50:
        return '(25, 50]'
    elif num <= 75:
        return '(50, 75]'
    else:
        return '(75, 100]'


def main():
    num = float(input())

    if esta_no_intervalo(num):
        intervalo = obter_intervalo(num)
        print(f'Intervalo {intervalo}')
    else:
        print('Fora de intervalo')

main()        