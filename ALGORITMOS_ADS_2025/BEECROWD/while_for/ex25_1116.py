def obter_divisao(valor1, valor2):
    try:
        divisao = valor1 / valor2
        return f'{divisao:.1f}'
    except ZeroDivisionError:
        return 'divisao impossivel'


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def exibir_resultados(n):
    for entrada in range(n):
        x, y = mapear(input().split(), int)
        print(obter_divisao(x, y))


def main():
    n = int(input())        
    exibir_resultados(n)

main()    