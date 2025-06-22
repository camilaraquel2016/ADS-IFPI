from utils import obterNumRealPositivo

def analisar_consumo(distancia_necessaria, qtd_litros_disponivel, distancia_percorrida = 0, qtd_litros_gastos = 0, contador = 1):
    print(f'-=-{contador}° medição-=-')
    contador += 1

    distancia_da_vez = obterNumRealPositivo('Distância percorrida desde a última medição: (Km) ')
    qtd_litros_da_vez = obterNumRealPositivo('Quantidade de litros consumidos para percorrer essa distância: ')

    distancia_percorrida += distancia_da_vez
    qtd_litros_gastos += qtd_litros_da_vez

    if distancia_percorrida < distancia_necessaria:
        return analisar_consumo(distancia_necessaria, qtd_litros_disponivel, distancia_percorrida, qtd_litros_gastos, contador)
    
    print('Chegou ao destino!')
    qtd_media_km_por_litro = distancia_percorrida / qtd_litros_gastos
    qtd_de_litros_para_distancia_necessaria = distancia_necessaria / qtd_media_km_por_litro

    if qtd_de_litros_para_distancia_necessaria > qtd_litros_disponivel:
        print(f'Para percorrer {distancia_necessaria} Km foram necessários {qtd_de_litros_para_distancia_necessaria:.1f} litros, ou seja, o carro precisou abastecer no caminho')
    else:
        print(f'Para percorrer {distancia_necessaria} Km foram necessários {qtd_de_litros_para_distancia_necessaria:.1f} litros, ou seja, o carro não precisou abastecer no caminho')
            
def main():
    distancia_necessaria = 600
    qtd_litros_disponivel = 50
    analisar_consumo(distancia_necessaria, qtd_litros_disponivel, 0, 0, 1)

main()    



