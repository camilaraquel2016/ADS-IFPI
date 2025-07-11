def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def obter_qtd_leds(numero: str, valores_leds: dict):
    numero = mapear(numero, int)
    qtd_leds = 0

    for valor in numero:
        qtd_leds += valores_leds[valor]

    return qtd_leds    



def repetir(n, valores_leds):
    for caso in range(n):
        numero = input()
        qtd_leds = obter_qtd_leds(numero, valores_leds)
        print(f'{qtd_leds} leds')


def main():
    valores_leds = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    qtd_casos = int(input())
    repetir(qtd_casos, valores_leds)

main()    