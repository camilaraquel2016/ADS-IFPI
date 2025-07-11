def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def exibir_linha(linha):
    linha_formatada = ''

    for num in linha:
        linha_formatada += f'{num} '

    print(linha_formatada.strip())    


def exibir_numeros(x, y): 
    linha = []

    for i in range(1, y + 1, 1): 
        linha.append(i) 

        if len(linha) == x:
            exibir_linha(linha)
            linha = []

        elif i == y:
            exibir_linha(linha)


def main():
    x, y = mapear(input().split(), int)
    exibir_numeros(x, y)

main() 


