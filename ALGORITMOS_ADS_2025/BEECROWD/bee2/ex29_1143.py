def exibir_numeros(qtd_numeros):
    for numero in range(1, qtd_numeros + 1):
        print(f'{numero} {numero ** 2} {numero ** 3}')


def main():
    n = int(input())
    exibir_numeros(n)  

main()