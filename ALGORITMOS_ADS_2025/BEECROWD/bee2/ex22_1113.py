def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))


    return nova_colecao


def obter_resultados():
    while True:
        x, y = mapear(input().split(), int)

        if x == y:
            break
        elif y > x:
            print('Crescente')
        else:
            print('Decrescente')    


def main():
    obter_resultados()

main()            