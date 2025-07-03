def exibir_elementos(colecao):
    for item in colecao:
        print(item, end = ' ')


def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def somar(n1, n2):
    return n1 + n2


def obter_resultados():
    while True:
        m, n = mapear(input().split(), int)

        if m <= 0 or n <= 0:
            break

        lista_ordinaria = range(obter_menor(m, n), obter_maior(m, n) + 1)
        exibir_elementos(lista_ordinaria)
        soma = reduzir(lista_ordinaria, somar, 0)
        print(f'Sum={soma}')

        
def main():
    obter_resultados()

main()    

