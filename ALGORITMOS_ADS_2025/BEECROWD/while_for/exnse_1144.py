def exibir_sequencias(n):
    for i in range(1, n + 1):
        valor1 = i
        valor2 = valor1 ** 2 
        valor3 = valor1 ** 3
        print(f'{valor1} {valor2} {valor3}')
        print(f'{valor1} {valor2 + 1} {valor3 + 1}')


def main():
    n = int(input())
    exibir_sequencias(n)

main()    
    
    