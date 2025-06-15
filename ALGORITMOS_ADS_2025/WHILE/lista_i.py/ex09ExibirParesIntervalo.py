from utils import obterNumInt

def listarParesIntevalo(limiteInferior, limiteSuperior):
    num = limiteInferior

    while num <= limiteSuperior:
        if num % 2 == 0:
            print(f'--> {num}')
        num += 1


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteSuperior = obterNumInt('Limite superior: ')

    print(f'-=-Números pares de {limiteInferior} a {limiteSuperior}-=-')
    listarParesIntevalo(limiteInferior, limiteSuperior)

main()   



