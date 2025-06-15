from utils import entradaFloat

def menorValor(valor1, valor2, valor3):
    menor = valor1
    if valor2 < menor:
        menor = valor2
    if valor3 < menor:
        menor = valor3

    return menor


def pedirProduto(num):
    return str(input(f'Qual nome do {num} produto? '))


def pedirValor(num):
    return entradaFloat(f'Qual valor do {num} produto? R$')


def produtoMenorValor(prod1, prod2, prod3, valor1, valor2, valor3):
    valorMenor = menorValor(valor1, valor2, valor3)

    return prod1 if valor1 == valorMenor else prod2 if valor2 == valorMenor else prod3


def main():
    produto1 = pedirProduto('primeiro')
    valorProduto1 = pedirValor('primeiro')

    produto2 = pedirProduto('segundo')
    valorProduto2 = pedirValor('segundo')

    produto3 = pedirProduto('terceiro')
    valorProduto3 = pedirValor('terceiro')

    valorMenor = menorValor(valorProduto1, valorProduto2, valorProduto3)

    produtoMaisEmConta = produtoMenorValor(produto1, produto2, produto3, valorProduto1, valorProduto2, valorProduto3)

    print(f'O produto mais barato é "{produtoMaisEmConta}" no valor de R${valorMenor:.2f}')


main()    


    