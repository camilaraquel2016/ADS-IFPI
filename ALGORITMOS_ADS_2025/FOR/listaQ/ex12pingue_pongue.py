from time import sleep
from itertools import count
from utils import obter_inteiro_positivo, obter_inteiro_no_intervalo

def calcular_diferenca(n1, n2):
    return n1 - n2 if n1 > n2 else n2 - n1


def exibir_vencedor(total_jog_1, total_jog_2):
    if total_jog_1 > total_jog_2:
        vencedor = 'JOGADOR 1'
    elif total_jog_2 > total_jog_1:
        vencedor = 'JOGADOR 2'

    return f'''
    jogador 1: {total_jog_1} pontos
    jogador 2: {total_jog_2} pontos
    vencedor: {vencedor}
    '''    

def espaco():
    print( )


def obter_vencedor():
    total_jog_1 = 0
    total_jog_2 = 0

    for rodada in count():
        print(f'-=-=-=-=-=-=-{rodada + 1}° RODADA-=-=-=-=-=-')
        quem_ganhou = obter_inteiro_no_intervalo(f'Quem ganhou o ponto?\nDigite 1 para jogador 1 e 2 para jogador 2: ', 1, 2)
        sleep(1)
        espaco()

        if quem_ganhou == 1:
            total_jog_1 += 1
        else:
            total_jog_2 += 1    

        diferenca = calcular_diferenca(total_jog_1, total_jog_2)

        if (total_jog_1 == 21 or total_jog_2 == 21) and diferenca >= 2:
            return exibir_vencedor(total_jog_1, total_jog_2)

        if (total_jog_1 > 21 or total_jog_2 > 21) and diferenca == 2:
            return exibir_vencedor(total_jog_1, total_jog_2)
            

def main():
    print(f'-=-CAMPEONATO PINGUE-PONGUE PI-=-')
    obter_vencedor()
     

main()








