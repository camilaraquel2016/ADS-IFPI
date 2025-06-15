from time import sleep

from utils import entradaInt, entradaFloat, validarLimiteMinFloat

def vazio():
    print(' ')


def menu():
    print('(1) - Adição\n(2) - Subtração\n(3) - Multiplicação\n(4) - Divisão')


def verificarN2(n2):
    if n2 != 0:
        return n2
    else:
        print('Entrada inválida! O número que será usado como dividendo não pode ser igual a 0')
        n2 = entradaFloat('Insira o segundo número: ')
        return verificarN2(n2)


def pedirOpcao():
    menu()
    vazio()
    opcao = entradaInt('Escolha uma opção (1 a 4) >>> ')
    if opcao >= 1 and opcao <= 4:
        return opcao
    else:
        print('Processando...')
        sleep(1)
        vazio()

        print('Opção inválida!')
        sleep(1)
        vazio()

        print('Vamos tentar novamente...')
        sleep(1)
        vazio()

        return pedirOpcao()


def operacao(n1, n2, opcao):
    match opcao:
        case 1:
            return f'{n1} + {n2} = {n1 + n2}'
        case 2:
            return f'{n1} - {n2} = {n1 - n2}'
        case 3:
            return f'{n1} * {n2} = {n1 * n2}'
        case 4:
            n2 = verificarN2(n2)
            return f'{n1} / {n2} = {n1 / n2:.2f}'
        

def main():
    n1 = entradaFloat('Insira o primeiro número: ')
    n2 = entradaFloat('Insira o segundo número: ')
    opcao = pedirOpcao()

    print(operacao(n1, n2, opcao))

main()