from random import randint
from utils import obterNumInteiro

def gerar_num(limite_min, limite_max):
    return randint(limite_min, limite_max)


def adivinhar(num_gerado, tentativas = 1):
    num_da_vez = obterNumInteiro('Insira seu palpite: ')

    if num_gerado > num_da_vez:
        print('É MAIOR!')
        return adivinhar(num_gerado, tentativas + 1)
    
    elif num_gerado < num_da_vez:
        print('É MENOR!')    
        return adivinhar(num_gerado, tentativas + 1)
    
    print(f'Muito bem você acertou!\nQuantidade de tentativas: {tentativas}')


def main():
    limite_min = 1
    limite_max = 50
    num_gerado = gerar_num(limite_min, limite_max)
    print(f'Pensei em um número entre {limite_min} e {limite_max}\nTente adivinhar...')
    adivinhar(num_gerado, 1)
    
main()