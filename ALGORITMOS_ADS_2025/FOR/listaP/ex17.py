#12:54
#12:59

def obter_valor_fracao(num):
    num += 1
    soma = 0

    for i in range(1, num, 1):
        soma += 1 / i

    return soma


def main():
    num = int(input('Valor de N: '))
    soma = obter_valor_fracao(num)
    print(f'A soma das frações é {soma:.2f}')

main()



