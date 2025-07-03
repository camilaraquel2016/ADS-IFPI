def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao

def calcular_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    return ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)


def repetir(qtd_vezes, peso1, peso2, peso3):
    for repeticao in range(qtd_vezes):
        nota1, nota2, nota3 = mapear(input().split(), float)
        media_ponderada = calcular_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)
        print(f'{media_ponderada:.1f}')
    


def main():
    peso1, peso2, peso3 = 2, 3, 5
    qtd_vezes = int(input())
    repetir(qtd_vezes, peso1, peso2, peso3)

main()