def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def sao_multiplos(num1, num2):
    maior = obter_maior(num1, num2)
    menor = obter_menor(num1, num2)

    return maior % menor == 0


def main():
    valores = input().split()

    num1 = int(valores[0])
    num2 = int(valores[1])

    if sao_multiplos(num1, num2):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

main()            