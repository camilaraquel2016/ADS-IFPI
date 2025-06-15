def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def obter_mdc(num1, num2):
    menor = obter_menor(num1, num2)
    final = menor + 1
   
    for i in range(1, final, 1):
        if num1 % i == 0 and num2 % i == 0:
            mdc = i

    return mdc


def main():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    mdc = obter_mdc(num1, num2)
    print(f'MDC DE ({num1}, {num2}) = {mdc}')

main()

