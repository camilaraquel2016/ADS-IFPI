from utils import obter_inteiro_maior_que_0, obterNumRealPositivo, obterNumInteiroPositivo

def saida(pontos_a, pontos_b):
    if pontos_a > pontos_b:
        resultado = 'Clube A ganhou!'
    elif pontos_b > pontos_a:
        resultado = 'Clube B ganhou!' 
    else:
        resultado = 'Empate'

    return f'''
    Clube A: {pontos_a} pontos
    Clube B: {pontos_b} pontos
    Resultado: {resultado}'''           


def obter_clube(label):
    clube = str(input(label)).upper()

    if clube == 'A' or clube == 'B':
        return clube
    
    print('Clube inválido!\nInsira novamente...')
    return obter_clube(label)


def obter_posicao(label):

    posicao = obter_inteiro_maior_que_0(label)

    if posicao == 1 or posicao == 2 or posicao == 3 or posicao == 4:
        return posicao
    
    print('Posição do nadador inválida!\nInsira novamente...')
    return obter_posicao(label)


def obter_pontos(posicao):
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
        

def extrair_pontos_na_partida(qtd_nadadores, contador = 0, pontos_a = 0, pontos_b = 0):

    if contador < qtd_nadadores:
        contador += 1 
        print(f'-=-{contador}° jogador-=-')
        nome = input('Nome do jogador: ')
        classificacao = obter_posicao('Classificação do jogador: (1 a 4) ')
        pontos = obter_pontos(classificacao)
        tempo = obterNumRealPositivo('Tempo: (s) ')
        clube = obter_clube('Clube do nadador: (A / B) ')

        if clube == 'A':
            pontos_a += pontos

        elif clube == 'B':
            pontos_b += pontos

        return extrair_pontos_na_partida(qtd_nadadores, contador, pontos_a, pontos_b)
    
    return pontos_a, pontos_b
            

def obter_resultado(pontos_a = 0, pontos_b = 0):

    num_da_prova = obterNumInteiroPositivo('Número da prova: ')
    qtd_nadadores = obterNumInteiroPositivo('Quantidade de nadadores: ')

    if num_da_prova != 0 or qtd_nadadores != 0:
        print(f'-=-Prova N°{num_da_prova}-=-')
        pontos_obtidos = extrair_pontos_na_partida(qtd_nadadores, 0, 0, 0)
        pontos_a_na_partida = pontos_obtidos[0]
        pontos_b_na_partida = pontos_obtidos[1]

        pontos_a += pontos_a_na_partida
        pontos_b += pontos_b_na_partida
        
        return obter_resultado(pontos_a, pontos_b)
    
    return saida(pontos_a, pontos_b)


def main():
    print('-=-COMPETIÇÃO DE NATAÇÃO-=-')
    print(obter_resultado(0, 0))

main()        

    





        
    

            
    