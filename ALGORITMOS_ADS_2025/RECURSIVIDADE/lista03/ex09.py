from utils import obterNumInteiro, obterNumInteiroLimiteMin

def obterPrimeiroPar(num):
    if num % 2 == 0:
        return num
    return num + 1

 
def exibirParesDoIntervalo(primeiroPar, limiteFinal):
    if primeiroPar > limiteFinal:
        return
    else:
        print(primeiroPar)
        return exibirParesDoIntervalo(primeiroPar + 2, limiteFinal)


def main():
    limiteInicial = obterNumInteiro('Limite inicial: ')
    limiteFinal = obterNumInteiroLimiteMin('Limite final: ', limiteInicial + 1)
    primeiroPar = obterPrimeiroPar(limiteInicial)

    print(f'-=-PARES NO INTERVALO ({limiteInicial} A {limiteFinal})-=-')
    exibirParesDoIntervalo(primeiroPar, limiteFinal)

main()



    