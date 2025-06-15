from itertools import count
from utils import obter_inteiro_positivo

def dividir_sucessivamente(num):
    for i in count():
        resultado = num / 2 
        
        if resultado < 1:
            return num
        
        num = resultado


def main():
    num = obter_inteiro_positivo('Insira um número: ')
    ultima_divisao = dividir_sucessivamente(num)
    print(f'Dividindo o número {num} sucessivamente por 2, seu último resultado inteiro será {ultima_divisao}')

main()     



