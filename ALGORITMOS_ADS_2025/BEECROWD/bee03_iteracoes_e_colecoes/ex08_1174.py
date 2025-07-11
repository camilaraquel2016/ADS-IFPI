def obter_matriz(qtd_entradas):
    matriz = {}

    for index in range(qtd_entradas):
        num = float(input())
        if num <= 10:
            matriz[index] = num

    return matriz
 

def exibir_matriz(matriz: dict):
    for posicao, valor in matriz.items():
        print(f'A[{posicao}] = {valor:.1f}')


def main():
    qtd_entradas = 100
    matriz = obter_matriz(qtd_entradas)
    exibir_matriz(matriz)

main()            



