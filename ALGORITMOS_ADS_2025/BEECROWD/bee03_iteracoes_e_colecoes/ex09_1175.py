def exibir_matriz(matriz: dict):
    for posicao, valor in matriz.items():
        print(f'N[{posicao}] = {valor}')


def obter_matriz(qtd_entradas):
    matriz = {}

    for chave in range(qtd_entradas):
        numero = int(input())
        matriz[chave] = numero

    return matriz    


def trocar_valores(matriz: dict):
    tamanho_matriz = len(matriz)
    qtd_trocas = tamanho_matriz // 2

    for troca in range(qtd_trocas):
        matriz[troca], matriz[tamanho_matriz - 1 - troca] = matriz[tamanho_matriz - 1 - troca], matriz[troca]

    return matriz    


def main():
    qtd_entradas = 20
    matriz = obter_matriz(qtd_entradas)
    matriz_trocada = trocar_valores(matriz)
    exibir_matriz(matriz_trocada)

main()    