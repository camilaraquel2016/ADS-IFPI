from utils import obterNumInteiro

def eh_maior(num1,num2):
    return num1 >= num2


def obter_maior(qtd_num, maior, contador):

    num = obterNumInteiro(f'Insira o {contador}° número: ')

    if eh_maior(num, maior): maior = num

    if qtd_num > 1:
        qtd_num -= 1
        contador += 1
        return obter_maior(qtd_num, maior, contador)

    return maior


def main():
    qtd_num = obterNumInteiro('Insira a quantidade de números: ')

    num = obterNumInteiro(f'Insira o 1° número: ')

    maior = obter_maior(qtd_num - 1, num, 2)

    print(f'O maior é {maior}')

main()