def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def somar(valor1, valor2):
    return valor1 + valor2


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


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def eh_impar(num):
    return num % 2 == 1


def repetir_processo(qtd_vezes):
    for vez in range(qtd_vezes):
        x, y = mapear(input().split(), int)
        colecao_de_impares = filtrar(range(obter_menor(x, y) + 1, obter_maior(x, y)), eh_impar)
        soma_dos_impares = reduzir(colecao_de_impares, somar, 0)
        print(soma_dos_impares)
         

def main():
    qtd_vezes = int(input())   
    repetir_processo(qtd_vezes)

main()
