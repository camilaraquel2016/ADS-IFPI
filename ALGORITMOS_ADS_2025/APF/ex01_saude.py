from utils import *

def espaco():
    print()


def obter_soma(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4


def saida(media_diaria, limite_cal_diario, maior_consumo_diario, dia_de_maior_consumo, menor_consumo_diario, dia_de_menor_consumo):
    print('-=' * 30)
    print(f'Média calórica do período: {media_diaria}')
    espaco()

    print(f'O dia de menor consumo calórico foi o dia "{dia_de_menor_consumo}" com consumo de {menor_consumo_diario} cal') 
    espaco()
    print(f'O dia de maior consumo calórico foi o dia "{dia_de_maior_consumo}" com consumo de {maior_consumo_diario} cal') 
    espaco()
    
    if media_diaria > limite_cal_diario:
        print(f'Que pena!...você excedeu o limite diário')
    else:
        print('Muito bem!...Você não excedeu o limite diário')


def imprimir_resultado_do_dia(dia, soma_do_dia):
        espaco()
        print(f'Média calórica do dia {dia} = {soma_do_dia}')
        espaco()


def imprimir_resultado(qtd_dias, limite_cal_diario):
    menor_consumo_diario = float('inf')
    maior_consumo_diario = 0
    total_cal = 0

    for dia in range(1, qtd_dias + 1, 1):
        
        print(f'-=-=-=-{dia}° dia-=-=-=-')
        cafe_da_manha = obter_num_real('Calorias no café da manhã: ')
        almoco = obter_num_real('Calorias no almoço: ')
        janta = obter_num_real('Calorias na janta: ')
        lanches = obter_num_real('Calorias nos lanches: ')

        soma_do_dia = obter_soma(cafe_da_manha, almoco, janta, lanches)
        
        imprimir_resultado_do_dia(dia, soma_do_dia)

        total_cal += soma_do_dia

        if soma_do_dia > maior_consumo_diario:
            maior_consumo_diario = soma_do_dia
            dia_de_maior_consumo = dia

        if soma_do_dia < menor_consumo_diario:
            menor_consumo_diario = soma_do_dia
            dia_de_menor_consumo = dia    

    media_diaria = total_cal / qtd_dias  

    saida(media_diaria, limite_cal_diario, maior_consumo_diario, dia_de_maior_consumo, menor_consumo_diario, dia_de_menor_consumo)
    

def main():
    qtd_dias = obter_num_inteiro('Quantidade de dias para análise: ')
    limite_cal_dia = obter_num_real('Qual seu limite calórico diário? ')
    espaco()
    imprimir_resultado(qtd_dias, limite_cal_dia)
    
    
main()    



