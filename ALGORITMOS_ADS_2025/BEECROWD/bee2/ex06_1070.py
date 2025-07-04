def eh_impar(num):
    return num % 2 == 1


def exibir_sequencia(x):
    x = x if eh_impar(x) else x + 1

    for numero in range(x, x + 11, 2):
        print(numero)


def main():
    x = int(input())
    exibir_sequencia(x)

main()    