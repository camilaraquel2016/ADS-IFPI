def obter_qtd_pontos(n):
    qtd_quadrado_em_cada_lado = 2 ** n
    qtd_pontos_lateral = qtd_quadrado_em_cada_lado + 1
    return qtd_pontos_lateral ** 2


def main():
    n = int(input())
    qtd_pontos = obter_qtd_pontos(n)
    print(qtd_pontos)

main()  

