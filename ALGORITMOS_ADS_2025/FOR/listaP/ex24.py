def saida(soma_salarios, soma_filhos, qtd_habitantes, qtd_salario_ate_1000):
    media_salario = soma_salarios / qtd_habitantes
    media_filhos = soma_filhos / qtd_habitantes
    percentual_salario_ate_1000 = qtd_salario_ate_1000 / qtd_habitantes * 100

    return f'''
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Média de salário: R${media_salario:.2f}
    Média de filhos: {media_filhos}
    Percentual de pessoas com salário de até R$ 1.000,00: {percentual_salario_ate_1000}%
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''


def imprimir_informacoes(qtd_habitantes):
    final = qtd_habitantes + 1
    soma_salarios = 0
    soma_filhos = 0
    qtd_salario_ate_1000 = 0

    for i in range(1, final, 1):
        print('-=' * 10)
        salario = float(input('Salário: R$'))
        qtd_filhos = int(input('Quantidade de filhos: '))

        soma_salarios += salario
        soma_filhos += qtd_filhos

        if salario <= 1000:
            qtd_salario_ate_1000 += 1

    print(saida(soma_salarios, soma_filhos, qtd_habitantes, qtd_salario_ate_1000))


def main():
    qtd_habitantes = int(input('Quantidade de habitantes: '))
    imprimir_informacoes(qtd_habitantes)

main()


