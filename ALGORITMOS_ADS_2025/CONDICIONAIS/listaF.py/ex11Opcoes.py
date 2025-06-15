from utils import entradaInt, validarNumLimiteInt

def escolherOpcao(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    

def main():

    num1 = entradaInt('Primeiro valor: ')
    num2 = entradaInt('Segundo valor: ')
    num3 = entradaInt('Terceiro valor: ')

    opcao = entradaInt('Escolha uma opção (1 a 3): ')
    opcao = validarNumLimiteInt(opcao, 1, 3, 'Escolha uma opção (1 a 3): ')

    res = escolherOpcao(opcao, num1, num2, num3)
    print(f'>> {res}')


main()

        