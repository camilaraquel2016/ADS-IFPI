# inicio 25/05 - 15:08
# fim 25/05
from q1_number_utils import obterNumInteiroPositivo, obterNumInteiroLimiteMin

def obterQtdDivisores(num):
    divisor = 1
    qtdDivisores = 0

    while divisor <= num:
        if num % divisor == 0:
            qtdDivisores += 1
        divisor += 1

    return qtdDivisores



def exibirResultado(valorA, valorB):
    while valorA <= valorB:
        qtdDivisores = obterQtdDivisores(valorA)
        print(f'Número: {valorA} - ({qtdDivisores}) divisores')
        valorA += 1


def main():
    valorA = obterNumInteiroPositivo('Primeiro valor: ')
    print('Lembrando que o próximo valor inserido deve ser maior que o primeiro pelo menos 11 unidades!') 
    valorB = obterNumInteiroLimiteMin('Segundo valor: ', valorA + 11)

    exibirResultado(valorA, valorB)

main()
