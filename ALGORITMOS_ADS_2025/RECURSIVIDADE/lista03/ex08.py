#11:28 
from utils import obterNumInteiro

def encontrarPrimeiroMultiplo(num, inicioIntervalo, contador = 1):
    multiplo = num * contador

    if multiplo >= inicioIntervalo:
        return multiplo
    else:
        return encontrarPrimeiroMultiplo(num, inicioIntervalo, contador + 1)
    

def exibirMultiplosDoIntervalo(limiteInicial, limiteFinal, num, primeiroMultiplo):
    if primeiroMultiplo > limiteFinal:
        return
    else:
        print(primeiroMultiplo)
        return exibirMultiplosDoIntervalo(limiteInicial, limiteFinal, num, primeiroMultiplo + num)
    

def main():
    limiteInicial = obterNumInteiro('Limite inicial: ')
    limiteFinal = obterNumInteiro('Limite final: ')
    num = obterNumInteiro('Valor de N: ')
    primeiroMultiplo = encontrarPrimeiroMultiplo(num, limiteInicial, 1)

    print(f'-=-MÚLTIPLOS DE {num} NO INTERVALO ({limiteInicial} A {limiteFinal})-=-')
    exibirMultiplosDoIntervalo(limiteInicial, limiteFinal, num, primeiroMultiplo)

main()
