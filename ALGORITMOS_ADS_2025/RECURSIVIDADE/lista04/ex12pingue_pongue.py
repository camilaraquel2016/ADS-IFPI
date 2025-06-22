from utils import obterNumInteiro

def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def obter_diferenca(num1, num2):
    maior = obter_maior(num1, num2)
    menor = obter_menor(num1, num2)
    return maior - menor


def obter_jogador(label):

    jogador = obterNumInteiro(label)

    if jogador == 1 or jogador == 2:
        return jogador

    print('Jogador invalido!\nInsira 1 ou 2')
    return obter_jogador(label)


def saida(pontos_jogador_1, pontos_jogador_2):
    if pontos_jogador_1 > pontos_jogador_2:
            ganhador = 'Jogador 1'
    else:    
            ganhador = 'Jogador 2'

    return f'''
    Pontos jogador 1: {pontos_jogador_1}
    Pontos jogador 2: {pontos_jogador_2}
    Vencedor: {ganhador}'''        


def obter_resultado(pontos_jogador_1 = 0, pontos_jogador_2 = 0):
    print(f'-=-=-=-=-Placar atual-=-=-=-=\njogador 1 - {pontos_jogador_1} X {pontos_jogador_2} - jogador 2\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    quem_levou_essa = obter_jogador('Qual jogador ganhou essa?\nJogador (1 ou 2)\n>>> ')

    if quem_levou_essa == 1:
        pontos_jogador_1 += 1
    else:
        pontos_jogador_2 += 1

    diferenca = obter_diferenca(pontos_jogador_1, pontos_jogador_2)
    primeira_condicao = (pontos_jogador_1 == 21 or pontos_jogador_2 == 21) and diferenca >= 2
    segunda_condicao = (pontos_jogador_1 > 21 or pontos_jogador_2 > 21) and diferenca == 2

    if primeira_condicao or segunda_condicao:
         return saida(pontos_jogador_1, pontos_jogador_2)
    
    return obter_resultado(pontos_jogador_1, pontos_jogador_2)


def main():
     print(obter_resultado(0, 0))

main()

    


