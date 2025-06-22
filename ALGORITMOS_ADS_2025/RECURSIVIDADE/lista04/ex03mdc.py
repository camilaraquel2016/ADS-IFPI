from utils import obter_inteiro_maior_que_0, eh_divisor


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def repetir(num1, num2, menor, candidato_mdc = 2, mdc = 1):

    if candidato_mdc < menor:
        if eh_divisor(candidato_mdc, num1) and eh_divisor(candidato_mdc, num2):
            mdc = candidato_mdc

        return repetir(num1, num2, menor, candidato_mdc + 1, mdc)    

    return mdc    


def obter_mdc(num1, num2):
    menor = obter_menor(num1, num2)
    candidato_mdc = 1
    return repetir(num1, num2, menor, candidato_mdc)


def main():
    num1 = obter_inteiro_maior_que_0('Primeiro número: ')
    num2 = obter_inteiro_maior_que_0('Segundo número: ')
    mdc = obter_mdc(num1, num2)
    print(f'MDC de ({num1}, {num2}) = {mdc}')

main()