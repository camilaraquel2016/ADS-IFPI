from utils import obter_inteiro_maior_que_0
from random import randint
from itertools import count

def gerar_num(limite_min, limite_max):
    return randint(limite_min, limite_max)


def adivinhar_num(num_sorteado, limite_min, limite_max):

    for tentativa in count(1):
        num_da_vez = obter_inteiro_maior_que_0(f'Tente advinhar o número sorteado entre {limite_min} e {limite_max}\n>>> ')

        if num_sorteado > num_da_vez:
            print('É maior')

        elif num_sorteado < num_da_vez:
            print('É menor')

        else:
            print(f'Muito bem...vc acertou na {tentativa}° tentativa')
            break 


def main():
    limite_min = 1
    limite_max = 50
    num_sorteado = gerar_num(limite_min, limite_max)
    
    adivinhar_num(num_sorteado, limite_min, limite_max)

main()
