from utils import obterNumInt

def listarImpares(limiteInferior, limiteSuperior):
    num = limiteInferior

    while num <= limiteSuperior:
        if not num % 2 == 0:
            print(f'--> {num}')
        num += 1


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteSuperior = obterNumInt('Limite superior: ')

    print(f'-=-ÍMPARES DE {limiteInferior} A {limiteSuperior}-=-')
    listarImpares(limiteInferior, limiteSuperior)

main()
 
