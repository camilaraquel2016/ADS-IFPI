from utils import obterNumInt

def obterDiferenca(n1, n2):
    return n1 - n2 if n1 > n2 else n2 - n1

def obterMaior(n1, n2):
    return n1 if n1 > n2 else n2



def encontrarGanhador():
    totalJogador1 = 0
    totalJogador2 = 0

    while True:
        pontosJogador1 = obterNumInt('Pontos do jogador 1: ')
        print(pontosJogador1)
        totalJogador1 += pontosJogador1
        print(totalJogador1)
        pontosJogador2 = obterNumInt('Pontos do jogador 2: ')
        print(pontosJogador2)
        totalJogador2 += pontosJogador2
        print(totalJogador2)
        diferenca = obterDiferenca(totalJogador1, totalJogador2)
        print(diferenca)
        if (totalJogador1 == 21 or totalJogador2 == 21) and diferenca >= 2:
            break
        if (totalJogador1 > 21 or totalJogador2 > 21) and diferenca == 2:
            break
    maior = obterMaior(totalJogador1, totalJogador2)
    print(maior)         


encontrarGanhador()