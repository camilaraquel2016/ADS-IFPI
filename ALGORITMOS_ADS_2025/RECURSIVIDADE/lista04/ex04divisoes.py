from utils import obter_inteiro_maior_que_0

def dividir_sucessivamente(num):

    if num >= 1:
        num /= 2
        return dividir_sucessivamente(num)
    
    return num


def main():
    num = obter_inteiro_maior_que_0('Insira um número: ')
    resposta = dividir_sucessivamente(num)
    print(f'O resultado é {resposta}')

main()    
