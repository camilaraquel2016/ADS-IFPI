from utils import obterNumInt

def exibirDivisores(num: int):
    divisor = 1
    
    while divisor <= num:
        if num % divisor == 0:
            print(divisor, end = '')
            if divisor != num:
                print(',', end = ' ')
        divisor += 1   


def controlarExibiçao():
    resposta = 1

    while resposta != 0:
        num = obterNumInt('Qual número deseja analisar? ')
        print(f'Os divisores de {num} são: ', end = '')
        exibirDivisores(num)
        resposta = obterNumInt('\nDigite 0 para sair ou outro número para continuar: ')


def main():
    print('-=-=-=-ANALISADOR DE DIVISORES-=-=-=-')
    controlarExibiçao()
    print('Programa encerrado...')

main()    
