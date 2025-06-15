from utils import obterNumInteiro

def exibir_intervalo(limite_final):
    for num in range(1, limite_final + 1, 1):
        print(num)


def main():
    limite_final = obterNumInteiro('Limite final: ')
    print(f'-=-INTERVALO DE 1 A {limite_final}-=-')
    exibir_intervalo(limite_final)

main()            


