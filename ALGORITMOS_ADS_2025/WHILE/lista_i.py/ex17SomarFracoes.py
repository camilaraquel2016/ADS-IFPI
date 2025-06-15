def somarFracoes(num):
    divisor = 1
    soma = 0

    while divisor <= num:
        resultadoFracao = 1 / divisor
        soma += resultadoFracao
        divisor += 1
    return soma 


def main():
    num = int(input('Valor de N: '))
    somaDasFracoes = somarFracoes(num)
    print(f'A soma de frações indo até o divisor {num} é {somaDasFracoes:.2f}')

main()    