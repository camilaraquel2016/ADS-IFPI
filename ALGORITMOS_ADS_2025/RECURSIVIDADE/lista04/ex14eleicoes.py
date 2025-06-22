from utils import obterNumInteiro

def menu():
    return f'''
    45 - Serra
    13 - Dilma
    23 - Ciro Gomes
    
    99 - Indeciso
    98 - Outro
    0 - Nulo / Branco'''


def obter_voto(label):
    voto = obterNumInteiro(label)

    if voto == 45 or voto == 13 or voto == 23 or voto == 99 or voto == 98 or voto == 0 or voto == -1:
        return voto
    
    print('Voto inválido!\nInsira novamente...')
    return obter_voto(label)


def saida(total_serra, total_dilma, total_ciro, total_outros, total_indeciso, total_nulo, total_entrevistados):
    if total_serra > total_dilma and total_serra > total_ciro:
        resposta = 'NÃO'
    elif total_dilma > total_serra and total_dilma > total_ciro:
        resposta = 'NÃO' 
    elif total_ciro > total_serra and total_ciro > total_dilma:
        resposta = 'NÃO'
    else:
        resposta = 'SIM'  

    return f'''
    Serra: {total_serra / total_entrevistados * 100:.1f}%
    Dilma: {total_dilma / total_entrevistados * 100:.1f}%
    Ciro: {total_ciro / total_entrevistados * 100:.1f}%
    Outros: {total_outros / total_entrevistados * 100:.1f}%
    Indeciso: {total_indeciso / total_entrevistados * 100:.1f}%
    Nulo / Branco: {total_nulo / total_entrevistados * 100:.1f}%
    Terá segundo turno? {resposta}
'''


def obter_resultado(total_serra = 0, total_dilma = 0, total_ciro = 0, total_outros = 0, total_indeciso = 0, total_nulo = 0, total_entrevistados = 0):
    
    print(menu())
    voto = obter_voto('Insira seu voto: (flag = -1) ')

    match voto:
        case 45:
            total_serra += 1
        case 13:
            total_dilma += 1
        case 23:
            total_ciro += 1
        case 99:
            total_indeciso += 1
        case 98:
            total_outros += 1
        case 0:
            total_nulo += 1
        case -1:
            if total_entrevistados > 0:
                return saida(total_serra, total_dilma, total_ciro, total_outros, total_indeciso, total_nulo, total_entrevistados)
            return 'NENHUM ENTREVISTADO!'

    total_entrevistados += 1
    return obter_resultado(total_serra, total_dilma, total_ciro, total_outros, total_indeciso, total_nulo, total_entrevistados)
                            
    
def main():
    print('-=-ELEIÇÕES 2025-=-')
    print(obter_resultado(0, 0, 0, 0, 0, 0, 0))

main()    