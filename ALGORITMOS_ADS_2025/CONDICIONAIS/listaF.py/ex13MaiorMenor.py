from utils import entradaInt

def maiorNum(n1, n2, n3, n4, n5):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    return maior


def menorNum(n1, n2, n3, n4, n5):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    return menor


def main():
    n1 = entradaInt('Primeiro número: ')
    n2 = entradaInt('Segundo número: ')
    n3 = entradaInt('Terceiro número: ')
    n4 = entradaInt('Quarto número: ')
    n5 = entradaInt('Quinto número: ')

    maior = maiorNum(n1, n2, n3, n4, n5)
    menor = menorNum(n1, n2, n3, n4, n5)

    print('-=' * 10)

    print(f'Maior número: {maior}\nMenor número: {menor}')


main()    