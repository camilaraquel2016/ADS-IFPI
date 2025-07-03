def exibir_numeros(n):
    for numero in range(1, 10001):
        if numero % n == 2:
            print(numero)


def main():
    n = int(input())
    exibir_numeros(n)

main()    