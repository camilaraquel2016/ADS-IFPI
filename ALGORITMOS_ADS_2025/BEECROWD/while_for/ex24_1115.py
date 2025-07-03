def eh_nulo(num):
    return num == 0


def eh_positivo(num):
    return num > 0


def obter_quadrante(x, y):
    if eh_positivo(x):
        if eh_positivo(y):
            return 'primeiro'
        return 'quarto'
    else:
        if eh_positivo(y):
            return 'segundo'
        return 'terceiro'


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao


def obter_resultados():
    while True:
        x, y = mapear(input().split(), int)

        if eh_nulo(x) or eh_nulo(y):
            break

        quadrante = obter_quadrante(x, y)
        print(quadrante)


def main():
    obter_resultados()

main()    
