from utils import obterNumInteiro, obterNumInteiroLimiteMin

def exibirPA(limiteInicial, limiteFinal, razao):
    if limiteInicial < limiteFinal:
        print(limiteInicial)
        exibirPA(limiteInicial + razao, limiteFinal, razao)

        
def main():
    limiteInicial = obterNumInteiro('Limite inicial: ')
    limiteFinal = obterNumInteiroLimiteMin('Limite final: ', limiteInicial + 1)
    razao = obterNumInteiroLimiteMin('Razão: ', 1)

    exibirPA(limiteInicial, limiteFinal, razao)

main()    
