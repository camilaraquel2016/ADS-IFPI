from utils import obterNumInt


def obterClubeDeOrigem(label):
    while True:
        clube = str(input(label)).upper()
        if clube == 'A' or clube == 'B':
            return clube
        else:
            print('Clube inválido!')

def extrairPontos(classficacao):
    if classficacao == 1:
        return 9
    if classficacao == 2:
        return 6
    if classficacao == 3:
        return 4
    if classficacao == 4:
        return 3


def obterPosicao(label):
    
    while True:
        posicao = obterNumInt(label)
        if posicao == 1 or posicao == 2 or posicao == 3 or posicao == 4:
            return posicao
        else:
            print('Posição inválida!')


    
def somaDePontosPorProva(qtdDeNadadores):
    somaClubeA = 0
    somaClubeB = 0
    contador = 1 

    while contador <= qtdDeNadadores:
        nomeNadador = str(input(f'Nome do {contador}° nadador: '))
        classificaoDoNadador = obterPosicao(f'Número da posição final do {contador}° nadador: ')
        tempo = float(input('Tempo que concluiu a prova: '))
        clubeOrigem = obterClubeDeOrigem('Pertence a qual clube? ("A" ou "B") ')
        pontos = extrairPontos(classificaoDoNadador)
        if clubeOrigem == 'A':
            somaClubeA += pontos
        if clubeOrigem == 'B':
            somaClubeB += pontos    

        contador += 1
        
    return somaClubeA, somaClubeB


def gerenciarCompeticao():
    pontosTotaisClubeA = 0
    pontosTotaisClubeB = 0
    numeroDaProva = obterNumInt('Número da prova: (flag = 0) ')

    while numeroDaProva != 0:
        qtdDeNadadores = obterNumInt('Quantidade de nadadores nessa prova: ')
        qtdDepontos = somaDePontosPorProva(qtdDeNadadores)
        qtdDePontosClubeA = qtdDepontos[0]
        qtdDePontosClubeB = qtdDepontos[1]
        pontosTotaisClubeA += qtdDePontosClubeA
        pontosTotaisClubeB += qtdDePontosClubeB
        numeroDaProva = obterNumInt('Número da prova: (flag = 0) ')

    if pontosTotaisClubeA == 0 and pontosTotaisClubeB == 0:
        return     

    return pontosTotaisClubeA, pontosTotaisClubeB


def ganhador(pontosA, pontosB):
    return 'clube A ganhou' if pontosA > pontosB else 'clube B ganhou' if pontosB > pontosA else 'empate'





def main():
    print('-=-COMPETIÇÃO DE NATAÇÃO-=-')
    pontosTotais = gerenciarCompeticao()

    if pontosTotais == None:
        print('NENHUMA PROVA CADASTRADA!')
    else:
        pontosDeA = pontosTotais[0]
        pontosDeB = pontosTotais[1]
        resultado = ganhador(pontosDeA, pontosDeB)
        print(f'Clube A - {pontosDeA} x Clube B - {pontosDeB}')
        print(f'Resultado: {resultado}')
        

main()    

    
