def obter_qtd_pecas(n):
    return (n + 1) * (n + 2) // 2


def main():
    n = int(input())
    qtd_pecas = obter_qtd_pecas(n)
    print(qtd_pecas)

main()    

