from utils import obter_inteiro_positivo


def obter_qtd_digitos(num):

    for i in range(1, num + 1, 1): 
        
        if num < 10:
            return i 
        
        num //= 10 


def main():
    num = obter_inteiro_positivo('Número: ')
    qtd_digitos = obter_qtd_digitos(num)
    print(f'O número {num} é composto por {qtd_digitos} dígito(s)')

main()