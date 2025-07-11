def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def obter_deslocamento(v, t):
    return v * t


def main():
    try:
        while True:
            valores = input()
            if not valores: 
                continue
            v, t = mapear(valores.split(), int)
            deslocamento = obter_deslocamento(v, t)
            print(deslocamento * 2)
    except EOFError:
        pass

main()
