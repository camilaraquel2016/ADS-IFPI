def eh_par(num):
    return num % 2 == 0

def exibir_pares(limite_inicial, limite_final):
    if not eh_par(limite_inicial):
        limite_inicial += 1

    limite_final += 1    

    for i in range(limite_inicial, limite_final, 2):
        print(i)


def main():
    limite_inicial = int(input('Limite inicial: '))
    limite_final = int(input('Limite final: '))

    print(f'-=-PARES NO INTERVALO ({limite_inicial} A {limite_final})-=-') 
    exibir_pares(limite_inicial, limite_final)

main()           

