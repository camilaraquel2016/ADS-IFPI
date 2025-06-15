from utils import obterNumInt
from itertools import count

def grande_espaco(qtd_linhas):
    for i in range(qtd_linhas):
        print( )
    

def encontrar_num(num):
    for i in count():
        num_da_vez = obterNumInt('Tente advinhar o número\n>> ')

        if num_da_vez == num:
            return 'Número encontrado!'
        
        print('Não foi dessa vez, tente de novo!')
        print( )


def main():
    num = obterNumInt('Insira um número: ')
    grande_espaco(40)
    print(encontrar_num(num))
   
main()    