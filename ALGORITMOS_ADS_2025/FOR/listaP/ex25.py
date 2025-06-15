# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

from utils import obterNumInteiro

def pedir_voto():
    print('1 - candidato 1\n2 - candidato 2\n3 - canditato 3\n9 - voto nulo\n0 - voto em branco')
    
    voto = obterNumInteiro('Seu voto: ')
    voto_condicao = voto != 1 and voto != 2 and voto != 3 and voto != 9 and voto != 0
    if(voto_condicao):
        print("VOTO INVÁLIDO")
        voto = pedir_voto()

    return voto


def obter_vencedor(votos_cand_1, votos_cand_2, votos_cand_3):
    if votos_cand_1 > votos_cand_2 and votos_cand_1 > votos_cand_3:
        return 'Vencedor --> Candidato 1'
    if votos_cand_2 > votos_cand_1 and votos_cand_2 > votos_cand_3:
        return 'Vencedor --> Candidato 2'
    if votos_cand_3 > votos_cand_2 and votos_cand_3 > votos_cand_1:
        return 'Vencedor --> Candidato 3'

    return 'EMPATE'



def saida(resultado, votos_nulo, votos_branco, votos_cand_1, votos_cand_2, votos_cand_3):
    return f'''
    Total candidato 1: {votos_cand_1}
    Total candidato 2: {votos_cand_2}
    Total candidato 3: {votos_cand_3}
    Total votos nulos: {votos_nulo}
    Total votos em branco: {votos_branco}
    RESULTADO: {resultado}
    '''
    

def analisar_votacao(qtd_eleitores):
    total_cand_1 = 0
    total_cand_2 = 0
    total_cand_3 = 0
    total_branco = 0
    total_nulo = 0

    for eleitor in range(0, qtd_eleitores, 1):
        voto = pedir_voto()

        match voto:
            case 1:
                total_cand_1 += 1
            case 2:
                total_cand_2 += 1
            case 3:
                total_cand_3 += 1
            case 9:
                total_nulo += 1
            case 0:
                total_branco += 1
            case _:
                print('Nenhum voto incrementado!')   

    resultado = obter_vencedor(total_cand_1, total_cand_2, total_cand_3)

    print(saida(resultado, total_nulo, total_branco, total_cand_1, total_cand_2, total_cand_3))
    

def main():
    qtd_eleitores = obterNumInteiro('Quantidade de eleitores: ')
    analisar_votacao(qtd_eleitores)

main()