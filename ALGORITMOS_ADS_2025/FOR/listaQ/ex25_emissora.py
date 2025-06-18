# questão que pode ser feita perfeitamente usando while, entretanto como é uma prática de FOR, 
# o mesmo será usado nessa questão com o auxílio da função count do módulo itertools 

from itertools import count
from utils import obter_inteiro_positivo, obter_num_inteiro

def esta_na_lista(valor, lista):

    for opcao in lista:
        if valor == opcao:
            return True

    return False    
        
        
def exibir_opcoes_de_canais():
    return f'''
    -=-=-=-=-
    CANAL 2
    CANAL 4
    CANAL 5
    CANAL 7
    CANAL 10
    -=-=-=-=-
'''

def obter_canal(label, opcoes_de_canais):
    print(exibir_opcoes_de_canais())

    for tentativa in count():
        canal = obter_num_inteiro(label)

        if canal == 0:
            return canal

        if esta_na_lista(canal, opcoes_de_canais):
            return canal
        
        print(f'Canal {canal} inválido!')


def calcular_percentual_formatado(parte, todo):
    return parte / todo * 100


def exibir_saida(tot_canal_2, tot_canal_4, tot_canal_5, tot_canal_7, tot_canal_10, total_telespectadores):
    if total_telespectadores == 0:
        return 'NENHUM TELESPECTADOR NA PESQUISA'

    return f'''
    Canal 2: {calcular_percentual_formatado(tot_canal_2, total_telespectadores):.1f}%
    Canal 4: {calcular_percentual_formatado(tot_canal_4, total_telespectadores):.1f}%
    Canal 5: {calcular_percentual_formatado(tot_canal_5, total_telespectadores):.1f}%
    Canal 7: {calcular_percentual_formatado(tot_canal_7, total_telespectadores):.1f}%
    Canal 10: {calcular_percentual_formatado(tot_canal_10, total_telespectadores):.1f}%'''


def obter_resultado(opcoes_de_canais):
    tot_canal_2 = 0
    tot_canal_4 = 0
    tot_canal_5 = 0
    tot_canal_7 = 0
    tot_canal_10 = 0
    total_telespectadores = 0

    for casa in count(1):

        num_canal = obter_canal(f'Insira o canal que a casa {casa} está assistindo: (flag = 0) ', opcoes_de_canais)

        if num_canal == 0:
            return exibir_saida(tot_canal_2, tot_canal_4, tot_canal_5, tot_canal_7, tot_canal_10, total_telespectadores)

        qtd_pessoas_assistindo = obter_inteiro_positivo(f'Quantidade de pessoas assistindo o canal {num_canal} nessa casa: ')

        total_telespectadores += qtd_pessoas_assistindo

        match num_canal:
            case 2:
                tot_canal_2 += qtd_pessoas_assistindo
            case 4:
                tot_canal_4 += qtd_pessoas_assistindo
            case 5:
                tot_canal_5 += qtd_pessoas_assistindo
            case 7:
                tot_canal_7 += qtd_pessoas_assistindo
            case 10:
                tot_canal_10 += qtd_pessoas_assistindo               


def main():
    opcoes_de_canais = (2, 4, 5, 7, 10) # uso de tuplas, visto que as opções de canais não serão alteradas
    resultado = obter_resultado(opcoes_de_canais)
    print(f'-=-RESULTADO PESQUISA DE AUDIÊNCIA-=-')
    print(resultado)

main()    





