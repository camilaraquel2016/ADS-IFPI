def exibir_pares(limite_final):
    for num in range(2, limite_final + 1, 2):
        print(num)


def main():
    limite_final = int(input('Limite final: '))   
    print(f'-=-PARES DE 1 A {limite_final}-=-')
    exibir_pares(limite_final)

main()    


