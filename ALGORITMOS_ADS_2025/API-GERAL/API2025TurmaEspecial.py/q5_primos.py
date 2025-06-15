from q1_number_utils import obterNumInteiroPositivo

# início - 25/05 - 08:33
# fim - 25/05 - 09:07

def obterMenor(n1, n2):
    return n1 if n1 < n2 else n2


def obterMaior(n1, n2):
    return n1 if n1 > n2 else n2


def obterQtdDivisores(num):
    candidatoDivisor = 1
    qtdDivisores = 0

    while candidatoDivisor <= num:
        if num % candidatoDivisor == 0:
            qtdDivisores += 1
        candidatoDivisor += 1
    return qtdDivisores


def ehPrimo(num):
    qtdDivisores = obterQtdDivisores(num)

    return qtdDivisores == 2


def verificarIntervalo(n1, n2):
    menor = obterMenor(n1, n2)
    maior = obterMaior(n1, n2)
    num = menor


    while num <= maior:
        if ehPrimo(num):
            print(f'{num} - É PRIMO')
        else:
            print(f'{num} - NÃO É PRIMO')

        num += 1


def main():
    n1 = obterNumInteiroPositivo('Primeiro número: ')
    n2 = obterNumInteiroPositivo('Segundo número: ')
    print(f'-=-Analisando primos de {n1} até {n2}-=-')
    verificarIntervalo(n1, n2)

main()



