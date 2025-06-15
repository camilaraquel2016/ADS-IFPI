def calcular_valores(qtd_valores):
    limite_final = qtd_valores + 1
    soma = 0

    for i in range(1, limite_final, 1):
        num = int(input(f'{i}° número: '))
        soma += num

    media = soma / qtd_valores
    return f'Soma: {soma}\nMédia: {media:.1f}'


def main():
    qtd_valores = int(input('Quantidade de valores: '))
    resultado = calcular_valores(qtd_valores)
    print(resultado)

main()


