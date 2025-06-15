from utils import entradaInt, validarNumLimiteInt

def calcularIdadeAnos(diaAtual: int, mesAtual: int, anoAtual: int, diaNasc: int, mesNasc: int, anoNasc: int):
    if mesAtual < mesNasc:
        return anoAtual - anoNasc - 1
    elif mesAtual > mesNasc:
        return anoAtual - anoNasc
    else:
        if diaAtual < diaNasc:
            return anoAtual - anoNasc - 1
        else:
            return anoAtual - anoNasc


def vazio():
    print(' ')


def main():
    print('-=-=-ANALISADOR DE IDADE-=-=-')

    vazio()

    print('-=-=-DATA ATUAL-=-=-')

    diaAtual = entradaInt('Insira o dia atual: ')
    diaAtual = validarNumLimiteInt(diaAtual, 1, 31, 'Insira o dia atual: ')

    mesAtual = entradaInt('Insira o mês atual: ')
    mesAtual = validarNumLimiteInt(mesAtual, 1, 12, 'Insira o mês atual: ')

    anoAtual = entradaInt('Insira o ano atual: ')
    anoAtual = validarNumLimiteInt(anoAtual, 1800, 3000, 'Insira o ano atual: ') 

    vazio()

    print('-=-=-DATA DE NASCIMENTO-=-=-')

    diaNasc = entradaInt('Insira o dia de nascimento: ')
    diaNasc = validarNumLimiteInt(diaNasc, 1, 31, 'Insira o dia de nascimento: ')

    mesNasc = entradaInt('Insira o mês de nascimento: ')
    mesNasc = validarNumLimiteInt(mesNasc, 1, 12, 'Insira o mês de nascimento: ')

    anoNasc = entradaInt('Insira o ano de nascimento: ')
    anoNasc = validarNumLimiteInt(anoNasc, 1800, 3000, 'Insira o ano de nascimento: ') 

    idade = calcularIdadeAnos(diaAtual, mesAtual, anoAtual, diaNasc, mesNasc, anoNasc)

    vazio()

    print(f'Para quem nasceu na data {diaNasc}/{mesNasc}/{anoNasc} tem atualmente {idade} anos')
 

main()


