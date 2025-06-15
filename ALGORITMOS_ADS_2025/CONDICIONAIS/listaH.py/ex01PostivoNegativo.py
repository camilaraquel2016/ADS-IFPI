from utils import entradaInt
from time import sleep

def numPositvoOuNegativo(num: int):
    return 'positivo' if num > 0 else 'negativo' if num < 0 else 'neutro'


def main():
    num = entradaInt('Qual número deseja analisa? ')
    print('Analisando número...')
    sleep(1)
    positivoNegativo = numPositvoOuNegativo(num)
    print(f'O número {num} é {positivoNegativo}')

main()    