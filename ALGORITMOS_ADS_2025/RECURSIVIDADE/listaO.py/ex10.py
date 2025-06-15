from utils import obterNumInteiroLimiteMin, obterNumInteiro


def obterPrimeiroImpar(num):
    if num % 2 == 0:
        return num + 1
    else:
        return num
    

def exbirImparesNoIntervalo(primeiroImpar, limiteFinal):
    if primeiroImpar > limiteFinal:
        return
    else:
        print(primeiroImpar)
        return exbirImparesNoIntervalo(primeiroImpar + 2, limiteFinal)
    

def main():
    limiteInicial = obterNumInteiro('Limite inicial: ')
    limiteFinal = obterNumInteiroLimiteMin('Limite final: ', limiteInicial + 1)
    primeiroImpar = obterPrimeiroImpar(limiteInicial)
    
    print(f'-=-ÍMPARES NO INTERVALO ({limiteInicial} A {limiteFinal})-=-')
    exbirImparesNoIntervalo(primeiroImpar, limiteFinal)

main()    