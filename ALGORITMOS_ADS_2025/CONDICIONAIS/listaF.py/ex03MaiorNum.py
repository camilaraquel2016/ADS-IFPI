from utils import entradaFloat

def maiorNum(n1, n2, n3):
    maior = n1
    if n2 > maior:
       maior = n2
    if n3 > maior:
       maior = n3
    return maior       


def main():
    n1 = entradaFloat('Digite o primeiro número: ')
    n2 = entradaFloat('Digite o segundo número: ')
    n3 = entradaFloat('Digite o terceiro número: ')

    maior = maiorNum(n1, n2, n3)
    print(f'A sequência ({n1}, {n2}, {n3}) tem como maior número o {maior}')

main()
