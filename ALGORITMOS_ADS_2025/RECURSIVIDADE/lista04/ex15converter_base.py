from utils import obterNumInteiro

def formatar_num(num):
    match num:
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'
        case _:
            return num


def repetir_bin(num, num_binario):
    if num == 0:

        return num_binario
    
    resto = num % 2
    num_binario = str(resto) + num_binario
    num //= 2

    return repetir_bin(num, num_binario)


def converter_para_bin(num):
    if num == 0:
        return 0
    
    num_binario = ''
    return repetir_bin(num, num_binario)


def repetir_hex(num, num_hexadecimal):
    if num == 0:
        return num_hexadecimal
    
    resto = formatar_num(num % 16)

    num_hexadecimal = str(resto) + num_hexadecimal
    num //= 16

    return repetir_bin(num, num_hexadecimal)


def converter_para_hex(num):
    if num == 0:
        return 0
    
    num_hexadecimal = ''
    return repetir_hex(num, num_hexadecimal)


def main():
    num = obterNumInteiro('Insira um número: ')
    num_binario = converter_para_bin(num) 
    num_hexadecimal = converter_para_hex(num)   
    print(f'Número {num}\nEm binário: {num_binario}\nEm hexadecimal: {num_hexadecimal}')

main()    