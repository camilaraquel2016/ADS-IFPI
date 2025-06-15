from utils import obterNumInt

def exibirValoresPA(limiteInferior: int, limiteSuperior: int, razao: int):
    num = limiteInferior
    
    if limiteInferior < limiteSuperior:
        while num <= limiteSuperior:
            print(f'--> {num}')
            num += razao
    elif limiteSuperior > limiteInferior:
        while num >= limiteSuperior:
            print(f'--> {num}')
            num -= razao    
    else:
        print(num)


def main():
    limiteInferior = obterNumInt('Limite inferior: ')
    limiteSuperior = obterNumInt('Limite superior: ')
    razao = obterNumInt('Razão da P.A: ')

    exibirValoresPA(limiteInferior, limiteSuperior, razao)

main()