def calcularKgMorango(qtdKg):
    return 2.5 if qtdKg <= 5 else 2.2


def calcularKgMaca(qtdKg):
    return 1.8 if qtdKg <= 5 else 1.5


def calcularValorFinal(qtdKgMorango, qtdKgMaca):
    percentualDesconto = 0
    valorKgMorango = calcularKgMorango(qtdKgMorango)
    valorKgMaca = calcularKgMaca(qtdKgMaca)

    valorTotal = (valorKgMorango * qtdKgMorango) + (valorKgMaca * qtdKgMaca)

    qtdKgTotais = qtdKgMaca + qtdKgMorango

    if qtdKgTotais > 8 or valorTotal > 25:
        percentualDesconto = 0.1
    return valorTotal - (valorTotal * percentualDesconto)


def main():
    kgMorango = float(input('Quantos Kg de morango? '))
    kgMaca = float(input('Quantos Kg de maçã? '))

    valorFinal = calcularValorFinal(kgMorango, kgMaca)

    print(f'{kgMorango} Kg de morango e {kgMaca} Kg de maçã\nTotal da compra: R${valorFinal:.2f}')

main()    

