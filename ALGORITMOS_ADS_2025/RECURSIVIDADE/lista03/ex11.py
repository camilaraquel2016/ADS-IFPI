from utils import obterNumInteiro, obterNumInteiroLimiteMin

def ehPrimo(num, divisor = 2):
    raizQuadrada = num ** 0.5
    
    if num < 2:
        return False

    if divisor > raizQuadrada:
        return True

    if num % divisor != 0:
        return ehPrimo(num, divisor + 1)
    
    return False


def exibirPrimos(limiteInicial, limiteFinal):
    if limiteInicial > limiteFinal:
        return
    
    if ehPrimo(limiteInicial):
        print(limiteInicial)

    return exibirPrimos(limiteInicial + 1, limiteFinal)    


def main():
    limiteInicial = obterNumInteiro('Limite inicial: ')
    limiteFinal = obterNumInteiroLimiteMin('Limite final: ', limiteInicial + 1)
    exibirPrimos(limiteInicial, limiteFinal)

main()    