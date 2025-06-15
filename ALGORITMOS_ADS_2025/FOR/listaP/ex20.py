#13:09

def eh_par(num):
    return num % 2 == 0


def somar_fracoes(num):
    final = num + 1
    numerador = 1
    soma = 1

    for denominador in range(2, final, 1):
        valor_da_fracao = numerador / denominador

        if eh_par(denominador):
            soma -= valor_da_fracao
        else:
            soma += valor_da_fracao

    return soma


def main():
    num = int(input('Valor de N: '))
    soma = somar_fracoes(num)

    print(f'A soma das frações é {soma:.2f}')

main()    






def main():
    num = int(input('Valor de N: '))
