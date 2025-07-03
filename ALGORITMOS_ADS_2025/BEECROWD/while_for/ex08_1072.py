def esta_no_intervalo(limite_min, limite_max, num):
    return num >= limite_min and num <= limite_max


def obter_resultados(limite_min, limite_max, qtd_vezes):
    dentro, fora = 0, 0

    for _ in range(qtd_vezes):
        numero = int(input())
        if esta_no_intervalo(limite_min, limite_max, numero):
            dentro += 1
        else:
            fora += 1

    return dentro, fora 

def main():
    limite_min, limite_max = 10, 20
    qtd_vezes = int(input())
    dentro, fora = obter_resultados(limite_min, limite_max, qtd_vezes)
    print(f'{dentro} in')
    print(f'{fora} out')

main()    


