

def somar_fracoes():
    final = 50 + 1
    numerador = 1
    soma = 0

    for denominador in range(1, final, 1):
        valor_da_fracao = numerador / denominador
        soma += valor_da_fracao

        numerador += 2

    return soma


def main():
    soma = somar_fracoes()

    print(f'A soma das frações é {soma:.2f}')

main()    
