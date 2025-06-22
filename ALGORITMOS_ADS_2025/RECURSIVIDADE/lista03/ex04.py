from utils import obterNumReal, obterNumRealLimiteMin

def exibirPG(limiteInicial, limiteFinal, razao):
    if limiteInicial < limiteFinal:
        print(limiteInicial)
        exibirPG(limiteInicial * razao, limiteFinal, razao)


def main():
    limiteInicial = obterNumReal('Limite inicial: ')
    limiteFinal = obterNumRealLimiteMin('Limite final: ', limiteInicial + 1)
    razao = obterNumRealLimiteMin('Razão: ', 2)
    exibirPG(limiteInicial, limiteFinal, razao)

main()    


