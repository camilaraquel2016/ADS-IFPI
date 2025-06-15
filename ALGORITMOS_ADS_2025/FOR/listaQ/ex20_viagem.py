from itertools import count
from utils import obter_real_positivo

def obter_resultado(qtd_litros_inicio, distancia_necessaria):
    tot_km_percorrido = 0
    tot_litros_gastos = 0

    for medicao in count():
        print(f'-=-{medicao + 1}° medição-=-')
        distancia_percorrida_da_vez = obter_real_positivo('Distância percorrida desde a última medição: (Km) ')
        qtd_litros_para_percorrer = obter_real_positivo(f'Quantidade de litros consumidos para percorrer esses {distancia_percorrida_da_vez} km: ')

        tot_km_percorrido += distancia_percorrida_da_vez
        tot_litros_gastos += qtd_litros_para_percorrer

        if tot_km_percorrido >= distancia_necessaria:
            print(f'Carro chegou ao seu destino!!!')

            consumo_medio = tot_km_percorrido / tot_litros_gastos

            print(f'Consumo médio: {consumo_medio} Km por litro')

            qtd_litros_necessaria_para_distancia_desejada = distancia_necessaria / consumo_medio

            if qtd_litros_necessaria_para_distancia_desejada <= qtd_litros_inicio:
                print(f'Carro conseguiu chegar ao destino com apenas {qtd_litros_necessaria_para_distancia_desejada} litros')

            else:
                print(f'Carro não conseguiu chegar ao destino com apenas {qtd_litros_inicio} litros, ele teve que usar {qtd_litros_necessaria_para_distancia_desejada} litros para percorrer os {distancia_necessaria} Km necessários')

            break  


def main():
    qtd_litros_inicio = 50
    distancia_necessaria = 600
    resultado = obter_resultado(qtd_litros_inicio, distancia_necessaria)

main()   