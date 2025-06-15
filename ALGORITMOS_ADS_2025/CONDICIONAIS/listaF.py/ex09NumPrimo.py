from utils import entradaInt, validarNumLimiteInt

def eh_primo(num):
    if num == 0 or num == 1:
        return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif (not num % 2 == 0) and (not num % 3 == 0) and (not num % 5 == 0) and (not num % 7 == 0):
        return True
    else:
        False


def main():

    num = entradaInt('Insira um número para analisar se é primo ou não: ')
    num = validarNumLimiteInt(num, 0, 100, 'Insira um número para analisar se é primo ou não: ')

    if eh_primo(num):
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} NÃO é primo')


main()

