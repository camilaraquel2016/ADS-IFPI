#09:23
#09:30

from utils import obterNumInteiroLimiteMin

def exibirIntervalo(numInicial, numFinal):
    print(numInicial)
    if numInicial < numFinal:
        return exibirIntervalo(numInicial + 1, numFinal)
    

def main():
    numFinal = obterNumInteiroLimiteMin('Insira o número final do intervalo: ', 2)
    exibirIntervalo(1, numFinal)

main()    


