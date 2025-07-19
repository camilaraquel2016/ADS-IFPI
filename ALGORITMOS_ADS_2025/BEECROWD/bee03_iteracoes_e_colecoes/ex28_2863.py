def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


def obter_menor(n1, n2):
    return n1 if n1 < n2 else n2


def obter_historico(qtd_entradas):
    historico = []

    for _ in range(qtd_entradas):
        historico.append(float(input()))

    return historico    


def main():
    try:
        while True:
            qtd_tentativas = int(input())
            historico = obter_historico(qtd_tentativas)
            menor_tempo = reduzir(historico, obter_menor, historico[0])
            print(menor_tempo)
            if not qtd_tentativas:
                break
    except (EOFError, ValueError):
        pass        

main()