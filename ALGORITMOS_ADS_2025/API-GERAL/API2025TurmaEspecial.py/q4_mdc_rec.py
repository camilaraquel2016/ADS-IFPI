#início 24/05 - 15:51
#fim 24/05 - 16:47

from q1_number_utils import obterNumInteiroPositivo

def obterMenor(n1, n2):
    return n1 if n1 < n2 else n2


def obterMDC(n1, n2, menor, candidatoDivisor = 1, mdc = 1):
        if candidatoDivisor <= menor:
            if n1 % candidatoDivisor == 0 and n2 % candidatoDivisor == 0:
                mdc = candidatoDivisor
            return obterMDC(n1, n2, menor, candidatoDivisor + 1, mdc)
        else: 
            return mdc


def main():
    n1 = obterNumInteiroPositivo('Primeiro número: ')
    n2 = obterNumInteiroPositivo('Segundo número: ')
    menor = obterMenor(n1, n2)
    mdc = obterMDC(n1, n2, menor, candidatoDivisor = 1, mdc = 1)
    print(f'MDC de ({n1}, {n2}) = {mdc}')

main()    
    