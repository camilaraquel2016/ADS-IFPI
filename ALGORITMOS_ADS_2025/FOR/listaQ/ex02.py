from itertools import count
from utils import obter_inteiro_positivo

def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2

 
def obter_mmc(num1, num2):
    maior = obter_maior(num1, num2)
    possivel_mmc = maior
    
    for i in count():
        if possivel_mmc % num1 == 0 and possivel_mmc % num2 == 0:
            return possivel_mmc
        
        possivel_mmc += maior


def main():
    n1 = obter_inteiro_positivo('Primeiro número: ')
    n2 = obter_inteiro_positivo('Segundo número: ')
    mmc = obter_mmc(n1, n2)
    print(f'MMC de ({n1}, {n2}) = {mmc}')

main()