def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def eh_impar(num):
    return num % 2 == 1


def somar(n1, n2):
    return n1 + n2


def reduzir(colecao, funcao_redutora, valor_incial):
    acumulado = valor_incial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


def obter_resultado(x, y):
    maior = obter_maior(x, y)
    menor = obter_menor(x, y)
    numeros_impares = filtrar(range(menor + 1, maior), eh_impar)
    soma = reduzir(numeros_impares, somar, 0)

    return soma
    

def main():
    x = int(input())
    y = int(input())
    soma = obter_resultado(x, y)
    print(soma)

main()    

