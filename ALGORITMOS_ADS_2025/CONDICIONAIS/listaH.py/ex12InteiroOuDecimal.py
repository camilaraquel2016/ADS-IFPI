def InteiroOuDecimal(num):
    quociente = num // 1
    return 'inteiro' if num == quociente else 'decimal'


def main():
    num = float(input('Insira o número: '))
    resposta = InteiroOuDecimal(num)
    print(f'O número {num} é {resposta}')

main()    