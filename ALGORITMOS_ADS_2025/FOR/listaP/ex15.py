def exibir_sequencia(qtd_termos):
    auxiliar = 0

    for i in range(1, qtd_termos + 1, 1):
        num = i + auxiliar
        print(num)
        auxiliar = num 


def main():
    n = int(input('Informe o valor de N: '))
    exibir_sequencia(n)


main()