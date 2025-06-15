from utils import obterNumInt, validarLimiteMin

def eh_primo(num):
    contador = 1
    qtdDivisores = 0

    while contador <= num:
       
        if num % contador == 0:
            qtdDivisores += 1
        contador += 1

    return qtdDivisores == 2


def listarPrimos(limiteInferior, limiteSuperior):
    num = limiteInferior

    while num <= limiteSuperior:
        if eh_primo(num):
            print(f'--> {num}')
        num += 1


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteInferior = validarLimiteMin(limiteInferior, 0, 'Limite inferior: ')

    limiteSuperior = obterNumInt('Limite superior: ')
    limiteSuperior = validarLimiteMin(limiteSuperior, 0, 'Limite superior: ')

    print(f'-=-NÚMEROS PRIMOS DE {limiteInferior} A {limiteSuperior}')

    listarPrimos(limiteInferior, limiteSuperior)

main()





