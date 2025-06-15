# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from API2023.utils import obterNumInteiro
from utils import obterNumInt
from itertools import count

def exibir_divisores(num):
    final = num + 1

    print(f'-=-DIVISORES DE {num}-=-')

    for divisor in range(1, final, 1):    
        if num % divisor == 0:
            print(divisor)


def exibir_num_com_divisores():
   
    for num in count():
        num = obterNumInt('Insira um número: (flag = 0) ')
        if num == 0:
            break
        
        exibir_divisores(num)


def main():
    exibir_num_com_divisores()   

main()


