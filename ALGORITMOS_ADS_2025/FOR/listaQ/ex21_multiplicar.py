from utils import obter_num_inteiro

def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2

def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def multiplicar(num1, num2):
    produto = 0

    maior = obter_maior(num1, num2)
    num_para_repetir = maior

    menor = obter_menor(num1, num2)
    qtd_vezes = menor + 1

    for vez in range(1, qtd_vezes, 1):
        produto += num_para_repetir

    return produto    


def main():
    print('Insira os dois valores que deseja multiplicar')
    num1 = obter_num_inteiro(f'Primeiro valor: ')
    num2 = obter_num_inteiro(f'Segundo valor: ')

    produto = multiplicar(num1, num2)

    print(f'{num1} x {num2} = {produto}')

main()    