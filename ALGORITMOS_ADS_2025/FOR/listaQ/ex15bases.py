from utils import obter_inteiro_no_intervalo
from itertools import count

def transformar_num(num):
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    
    return num
    

def converter_para_bin(num):
    if num == 0:
        return 0
    
    num_bin = ''

    for i in count():
        if num == 0:
            return int(num_bin)
        
        
        resto = num % 2
        num_bin = str(resto) + num_bin 

        num //= 2


def converter_para_hexadecimal(num):
    if num == 0:
        return 0
    
    num_hexadecimal = ''

    for i in count():
        if num == 0:
            return num_hexadecimal

        resto = transformar_num(num % 16)

        num_hexadecimal =  str(resto) + num_hexadecimal 

        num //= 16


def main():
    num = obter_inteiro_no_intervalo('Insira o número decimal que deseja converter: ', 0, 255)
    num_bin = converter_para_bin(num)
    num_hexa = converter_para_hexadecimal(num)

    print(f'{num} em binário: {num_bin}\n{num} em hexadecimal: {num_hexa}')
    
main()

