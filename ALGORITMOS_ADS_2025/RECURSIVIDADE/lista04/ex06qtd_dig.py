from utils import obter_inteiro_maior_que_0

def obter_qtd_dig(num, qtd_dig = 0):

    if num >= 1:
        qtd_dig += 1
        num //= 10
        return obter_qtd_dig(num, qtd_dig)
    
    return qtd_dig


def main():
    num = obter_inteiro_maior_que_0('Número: ')
    qtd_dig = obter_qtd_dig(num)
    print(f'O número {num} possui {qtd_dig} dígitos')

main()