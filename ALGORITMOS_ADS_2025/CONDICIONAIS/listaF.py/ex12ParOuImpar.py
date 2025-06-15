from utils import entradaInt

def parOuImpar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'ímpar'
    

def main():
    num = entradaInt('Insira um número para analisar se é par ou ímpar: ')

    res = parOuImpar(num)

    print(f'O número {num} é {res}')

main()        