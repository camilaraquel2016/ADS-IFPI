from utils import obterNumInt

def exibirValoresPG(limiteInferior: int, limiteSuperior: int, razao: int):
    num = limiteInferior

    if limiteInferior < limiteSuperior:
        while num <= limiteSuperior:
            print(f'--> {num}')
            num *= razao
    elif limiteInferior > limiteSuperior:
        while num >= limiteSuperior:
            print(f'--> {int(num)}')
            num /= razao 


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteSuperior = obterNumInt('Limite superior: ')
    razao = obterNumInt('Razão da P.G: ')

    exibirValoresPG(limiteInferior, limiteSuperior, razao)


main()                
        