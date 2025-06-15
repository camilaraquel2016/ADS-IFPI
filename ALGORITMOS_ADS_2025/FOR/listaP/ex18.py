#12:59
#13:08
def somar_fracoes(num):
    soma = 0
    denominador = num
    final = num + 1

    for numerador in range(1, final, 1):
        valor_da_fracao = numerador / denominador
        soma += valor_da_fracao

        denominador -= 1

    return soma    


def main():
    num = int(input('Valor de N: '))
    soma = somar_fracoes(num)

    print(f'A soma das frações é {soma:.2f}')

main()


    
