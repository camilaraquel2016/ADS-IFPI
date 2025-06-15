from itertools import count
from utils import obter_num_inteiro

def exibir_opcoes():
    return f'''
-=-=CANDIDATOS-=-=-
SERRA - 45
DILMA - 13
CIRO GOMES - 23

INDECISO - 99
OUTRO - 98
NULO / BRANCO - 0
-=-=-=-=-=-=-=-=-=-
'''

def obter_ganhador(votos_serra, votos_dilma, votos_ciro):
    if votos_serra > votos_dilma and votos_serra > votos_ciro:
        return 'SERRA GANHOU'

    if votos_dilma > votos_serra and votos_dilma > votos_ciro:       
        return 'DILMA GANHOU'
    
    if votos_ciro > votos_serra and votos_ciro > votos_dilma:
        return 'CIRO GOMES GANHOU'
    
    return '''EMPATE
    Possibilidade de 2° turno'''


def obter_voto():
    print(exibir_opcoes())

    while True:
        voto = obter_num_inteiro('Insira seu voto: (flag = -1) ')

        if voto == 45 or voto == 13 or voto == 23 or voto == 99 or voto == 98 or voto == 0 or voto == -1:
            return voto
        
        print(f'Voto inválido!\ninsira algum voto que está no menu de opções acima')


def exibir_resultado(votos_total, total_serra, total_dilma, total_ciro, total_indeciso, total_outros, total_nulo):
    if votos_total == 0:
        return 'NENHUM VOTO APRESENTADO' 
    
    resultado = obter_ganhador(total_serra, total_dilma, total_ciro)

    return f'''
    -=-=-RESULTADO VOTAÇÃO-=-=-
    SERRA: {total_serra / votos_total * 100:.1f}%
    DILMA: {total_dilma / votos_total * 100:.1f}%
    CIRO: {total_ciro / votos_total * 100:.1f}%
    INDECISO: {total_indeciso / votos_total * 100:.1f}%
    OUTROS: {total_outros / votos_total * 100:.1f}%
    NULO / BRANCO: {total_nulo / votos_total * 100:.1f}% 
    TOTAL DE ELEITORES: {votos_total} ELEITORES
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    
    RESULTADO FINAL: {resultado}
'''


def obter_resultado():
    tot_votos_serra = 0
    tot_votos_dilma = 0
    tot_votos_ciro = 0
    tot_votos_indeciso = 0
    tot_votos_nulos = 0
    tot_votos_outros = 0

    for eleitor in count():
        print(f'-=-{eleitor + 1}° ELEITOR-=-')
        voto = obter_voto()

        if voto == -1:
            return exibir_resultado(eleitor, tot_votos_serra, tot_votos_dilma, tot_votos_ciro, tot_votos_indeciso, tot_votos_outros, tot_votos_nulos)

        if voto == 45:
            tot_votos_serra += 1
        elif voto == 13:
            tot_votos_dilma += 1
        elif voto == 23:
            tot_votos_ciro += 1
        elif voto == 99:
            tot_votos_indeciso += 1
        elif voto == 98:
            tot_votos_outros += 1
        elif voto == 0:
            tot_votos_nulos += 1
    

def main():
    print(f'-=-ELEIÇÕES 2025-=-')
    print(obter_resultado())

main()
