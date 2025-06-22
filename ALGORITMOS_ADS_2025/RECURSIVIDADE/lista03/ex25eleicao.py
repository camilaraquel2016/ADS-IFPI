from utils import obter_inteiro_maior_que_0, obterNumRealPositivo


def menu():
    return f'''
    1 - Candidato 1
    2 - Candidato 2
    3 - Candidato 3
    9 - Nulo
    0 - Branco
'''


def obter_voto(label):

    voto = obterNumRealPositivo(label)

    if voto == 1 or voto == 2 or voto == 3 or voto == 9 or voto == 0:
        return voto 
    
    print('Voto inválido!\nInsira um voto válido')
    return obter_voto(label)


def obter_resultado(total_cand_1, total_cand_2, total_cand_3):
    if total_cand_1 > total_cand_2 and total_cand_1 > total_cand_3:
        return 'Candidato 1 ganhou!'
    elif total_cand_2 > total_cand_1 and total_cand_2 > total_cand_3:
        return 'Candidato 2 ganhou!'
    elif total_cand_3 > total_cand_1 and total_cand_3 > total_cand_2:
        return 'Candidato 3 ganhou!'
    else:
        return 'Empate'


def saida(total_cand_1, total_cand_2, total_cand_3, total_nulo, total_branco):
    resultado = obter_resultado(total_cand_1, total_cand_2, total_cand_3)

    return f'''
    Votos candidato 1: {total_cand_1}
    Votos candidato 2: {total_cand_2}
    Votos candidato 3: {total_cand_3}
    Votos em branco: {total_branco}
    Votos nulos: {total_nulo}

    Resultado: {resultado}'''


def obter_dados(qtd_eleitores, contador = 1, total_cand_1 = 0, total_cand_2 = 0, total_cand_3 = 0, total_nulo = 0, total_branco = 0):

    if contador <= qtd_eleitores:
        print(f'-=-=-{contador}° eleitor-=-=-')
        print(menu())
        voto = obter_voto('Insira seu voto: ')

        if voto == 1:
            total_cand_1 += 1
        elif voto == 2:
            total_cand_2 += 1
        elif voto == 3:
            total_cand_3 += 1
        elif voto == 9:
            total_nulo += 1
        else:
            total_branco += 1          

        return obter_dados(qtd_eleitores, contador + 1, total_cand_1, total_cand_2, total_cand_3, total_nulo, total_branco)
              
    return saida(total_cand_1, total_cand_2, total_cand_3, total_nulo, total_branco)



def main():
    qtd_eleitores = obter_inteiro_maior_que_0('Quantidade de eleitores: ')
    print(obter_dados(qtd_eleitores, 1, 0, 0, 0, 0, 0))

main()    
