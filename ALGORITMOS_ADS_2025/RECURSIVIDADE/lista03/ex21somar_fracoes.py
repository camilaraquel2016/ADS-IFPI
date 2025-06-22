def somar_fracoes(numerador = 1, denominador = 1, soma = 0):

    if denominador <= 50:
        resultado = numerador / denominador
        soma += resultado

        numerador += 2
        denominador += 1

        return somar_fracoes(numerador, denominador, soma)
    
    return soma


def main():
    soma = somar_fracoes(1, 1, 0)
    print(f'A soma é {soma:2f}')

main()    
    