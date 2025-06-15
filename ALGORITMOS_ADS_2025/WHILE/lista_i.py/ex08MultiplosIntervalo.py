from utils import obterNumInt

def encontrarPrimeiroMultiplo(limiteInferior, num):
    quociente = limiteInferior // num

    canditadoMultiplo = num * quociente

    if canditadoMultiplo == limiteInferior:
        return canditadoMultiplo
    else:
        canditadoMultiplo = num * (quociente + 1)
        return canditadoMultiplo


def exibirMultiplos(limiteInferior, limiteSuperior, num):
    numMultiplo = encontrarPrimeiroMultiplo(limiteInferior, num) # estado anterior 
    
    while numMultiplo <= limiteSuperior: # condição de continuidade
        print(f'--> {numMultiplo}') # trabalho
        numMultiplo += num # trabalho e convergência de dados


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteSuperior = obterNumInt('Limte superior: ')
    num = obterNumInt('Você deseja saber os múltiplos de qual número? ')

    print(f'-=-MÚLTIPLOS DE {num} NO INTERVALO {limiteInferior} A {limiteSuperior}')

    exibirMultiplos(limiteInferior, limiteSuperior, num)

main()    



