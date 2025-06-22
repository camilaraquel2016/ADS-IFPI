#09:50
#10:14
from utils import obterNumInteiroLimiteMin

def exibirPares(numInicial, numFinal): # o número inicial deve ser obrigariamente par
    if numInicial <= numFinal:
        print(numInicial)
        exibirPares(numInicial + 2, numFinal)
    
    
def ehPar(num):
    return num % 2 == 0


def exibirIntervaloPares(numInicial, numFinal):
    if not ehPar(numInicial): # ajuste do número inicial ser par
        numInicial += 1

    exibirPares(numInicial, numFinal)


def main():
    numFinal = obterNumInteiroLimiteMin('Insira o número final do intervalo: ', 2)
    print(f'-=-Pares entre 1 e {numFinal}-=-')
    exibirIntervaloPares(1, numFinal)

main()    





