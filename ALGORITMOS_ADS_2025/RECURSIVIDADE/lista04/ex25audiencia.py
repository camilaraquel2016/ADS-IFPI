from utils import obterNumInteiro, obter_inteiro_maior_que_0

def menu():
    return f'''
    -=-=-=-=-=-=
    Canal 2
    Canal 4
    Canal 5
    Canal 7 
    Canal 10
    -=-=-=-=-=-='''


def obter_canal(label):
    canal = obterNumInteiro(label)

    if canal == 2 or canal == 4 or canal == 5 or canal == 7 or canal == 10 or canal == 0:
        return canal
    
    print('Canal inválidoo!\nInsira novamente...')
    return obter_canal(label)


def saida(total_canal_2, total_canal_4, total_canal_5, total_canal_7, total_canal_10, total_entrevistados):
    if total_entrevistados == 0:
        return f'NENHUM ENTREVISTADO'
    
    return f'''
    Canal 2: {total_canal_2 / total_entrevistados * 100:.1f}%
    Canal 4: {total_canal_4 / total_entrevistados * 100:.1f}%
    Canal 5: {total_canal_5 / total_entrevistados * 100:.1f}%
    Canal 7: {total_canal_7 / total_entrevistados * 100:.1f}%
    Canal 10: {total_canal_10 / total_entrevistados * 100:.1f}%'''


def obter_dados(total_canal_2 = 0, total_canal_4 = 0, total_canal_5 = 0, total_canal_7 = 0, total_canal_10 = 0, contador = 1, total_entrevistados = 0):
    print(f'-=-{contador}° casa entrevistada-=-')
    print(menu())
    canal = obter_canal('Insira o canal: ')

    if canal == 0:
        return saida(total_canal_2, total_canal_4, total_canal_5, total_canal_7, total_canal_10, total_entrevistados) 
    
    qtd_pessoas = obter_inteiro_maior_que_0(f'Quantas pessoas assistem o canal {canal} nessa casa? ')
    total_entrevistados += qtd_pessoas

    match canal:
        case 2:
            total_canal_2 += qtd_pessoas
        case 4:
            total_canal_4 += qtd_pessoas
        case 5:
            total_canal_5 += qtd_pessoas
        case 7:
            total_canal_7 += qtd_pessoas
        case 10:
            total_canal_10 += qtd_pessoas

    return obter_dados(total_canal_2, total_canal_4, total_canal_5, total_canal_7, total_canal_10, contador + 1, total_entrevistados)                    


def main():
    print('-=-PESQUISA DE AUDIÊNCIA-=-')
    print(obter_dados(0, 0, 0, 0, 0, 1, 0))

main()    