from itertools import count
from utils import obter_inteiro_positivo, obter_num_inteiro, obter_inteiro_no_intervalo

def extrair_pontos(posicao):
    match posicao:
        case 1:
            return 9
        case 2:
            return 6
        case 3:
            return 4
        case 4:
            return 3
        case _:
            return 0
    

def obter_clube(label: str):

    while True:
        clube = str(input(label)).upper()

        if clube == 'A' or clube == 'B':
            return clube
        
        print('Entrada inválida!\nO clube inserido deve ser A ou B')


def exibir_resultado(pontos_a, pontos_b):
    print( )
    print(f'Clube A: {pontos_a}\nClube B: {pontos_b}')
    print('Resultado', end = ': ')

    if pontos_a > pontos_b:
        return f'Clube A venceu'
    elif pontos_b > pontos_a:
        return f'Clube B venceu'
    else:
        return 'EMPATE'


def enfeite_prova(num_da_prova: int):
    print( )
    print(f'-=-=-=-=PROVA N°{num_da_prova}-=-=-=-=-')


def enfeite_nadador(ordem_nadador: int):
    print( )
    print(f'-=-=-=-={ordem_nadador}° NADADOR-=-=-=-')


def competicao():
    pontos_a = 0
    pontos_b = 0

    for prova in count():
        print( )
        num_da_prova = obter_inteiro_positivo('Número da prova: ')
        qtd_nadadores = obter_inteiro_positivo('Quantidade de nadadores: ')
        
        for nadador in range(1, qtd_nadadores + 1):
            enfeite_prova(num_da_prova)
            enfeite_nadador(nadador)
            nome = str(input(f'Nome do {nadador}° nadador: '))
            classificacao = obter_inteiro_no_intervalo(f'Posição do nadador {nome}: ', 1, 4)
            pontos = extrair_pontos(classificacao)
            tempo = float(input('Tempo: (s) '))
            clube = obter_clube(f'Clube do nadador {nome}: (A OU B) ')
            
            if clube == 'A':
                pontos_a += pontos
            elif clube == 'B':
                pontos_b += pontos

        if num_da_prova == 0 and qtd_nadadores == 0:
            break

    if pontos_a == 0 and pontos_b == 0:
        return f'Nenhuma prova registrada!'        

    return exibir_resultado(pontos_a, pontos_b)



def main():
    print(f'-=-COMPETIÇÃO DE NATAÇÃO DO PI-=-')
    print(competicao())

main()    




