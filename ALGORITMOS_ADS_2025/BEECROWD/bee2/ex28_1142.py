def exibir_linha(valor_inicial):

    for valor in range(valor_inicial, valor_inicial + 3):
        print(valor, end = ' ')
        
    print('PUM')


def exibir_todas_as_linhas(n):
    valor_inicial = 1

    for linha in range(n):
        exibir_linha(valor_inicial)
        valor_inicial += 4


def main():
    n = int(input())
    exibir_todas_as_linhas(n)

main()    