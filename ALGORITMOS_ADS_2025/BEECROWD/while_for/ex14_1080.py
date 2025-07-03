def obter_resultado(qtd_numeros):
    maior = 0
    posicao_do_maior = 0

    for entrada in range(1, qtd_numeros + 1):
        numero = int(input())
        if numero > maior:
            maior = numero
            posicao_do_maior = entrada

    return maior, posicao_do_maior


def main():
    qtd_numeros = 100
    resultado = obter_resultado(qtd_numeros)
    maior, posicao_do_maior = resultado
    print(f'{maior}\n{posicao_do_maior}')

main()    



