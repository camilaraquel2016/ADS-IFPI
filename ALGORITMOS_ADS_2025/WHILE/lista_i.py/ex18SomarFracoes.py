def somarFracoes(num):
    numerador = 1
    denominador = num
    somaFracoes = 0

    while numerador <= num:
        resultado = numerador / denominador
        somaFracoes += resultado
        print(f'{numerador} / {denominador} = {resultado}')
        numerador += 1
        denominador -= 1
    return somaFracoes    

