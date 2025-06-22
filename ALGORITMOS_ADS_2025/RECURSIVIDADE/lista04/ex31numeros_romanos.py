from utils import obterNumInteiroPositivo

def obter_qtd_dig(num, qtd_dig = 0):
    qtd_dig += 1

    if num < 10:
        return qtd_dig
    
    num //= 10
    return obter_qtd_dig(num, qtd_dig)


def obter_num_de_ate_3_dig(label):
    num = obterNumInteiroPositivo(label)
    qtd_dig = obter_qtd_dig(num)

    if qtd_dig <= 3:
        return num
    
    print('Número imvalido!\nO número deve conter até 3 dígitos')
    return obter_num_de_ate_3_dig(label)


def obter_centena(num):
    return num // 100


def obter_dezena(num):
    return (num % 100) // 10


def obter_unidade(num):
    return num % 10


def simbolo_centena(centena):
    match centena:
        case 1:
            return 'C'
        case 2:
            return 'CC'
        case 3:
            return 'CCC'
        case 4:
            return 'CD'
        case 5:
            return 'D'
        case 6:
            return 'DC'
        case 7:
            return 'DCC'
        case 8:
            return 'DCCC'
        case 9:
            return 'CM'
        case _:
            return ''



def simbolo_dezena(dezena):
    match dezena:
        case 1:
            return 'X'
        case 2:
            return 'XX'
        case 3:
            return 'XXX'
        case 4:
            return 'XL'
        case 5:
            return 'L'
        case 6:
            return 'LX'
        case 7:
            return 'LXX'
        case 8:
            return 'LXXX'
        case 9:
            return 'XC'
        case _:
            return ''
        

def simbolo_unidade(unidade):
    match unidade:
        case 1:
            return 'I'
        case 2:
            return 'II'
        case 3:
            return 'III'
        case 4:
            return 'IV'
        case 5:
            return 'V'
        case 6:
            return 'VI'
        case 7:
            return 'VII'
        case 8:
            return 'VIII'
        case 9:
            return 'IX'
        case _:
            return ''
        

def converter_para_romano(num):
    centena = obter_centena(num)
    dezena = obter_dezena(num)
    unidade = obter_unidade(num)
    
    centena = simbolo_centena(centena)
    dezena = simbolo_dezena(dezena)
    unidade = simbolo_unidade(unidade)

    return centena + dezena + unidade


def main():
    num_decimal = obterNumInteiroPositivo('Insira o número decimal: ')
    num_romano = converter_para_romano(num_decimal)
    print(f'{num_decimal} = {num_romano}')

main()
