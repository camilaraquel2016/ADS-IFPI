from utils import obterNumInteiroNaFaixa

def obterValorCriterio(letra: str):
    return obterNumInteiroNaFaixa(f'Valor do critério {letra}: ', 0, 100)


def obterValorDoScore(valorMaximo, valorDoCriterio):
    return (valorDoCriterio / 100) * valorMaximo


def somarScore(scoreA, scoreB, scoreC):
    return scoreA + scoreB + scoreC


def classificarScoreAntigo(somaDosScore):
    if somaDosScore < 400:
        return 'Baixo'
    elif somaDosScore < 600:
        return 'Regular'
    elif somaDosScore < 800:
        return 'Bom'
    else:
        return 'Muito bom'
    

def classificarScoreNovo(somaDosScore):
    if somaDosScore <= 300:
        return 'Baixo'
    elif somaDosScore <= 500:
        return 'Regular'
    elif somaDosScore <= 700:
        return 'Bom'
    else:
        return 'Muito bom'


def main():
    valorCriterioA = obterValorCriterio('"a"')
    valorCriterioB = obterValorCriterio('"b"')
    valorCriterioC = obterValorCriterio('"c"')

    score1CriterioA = obterValorDoScore(260, valorCriterioA)
    score1CriterioB = obterValorDoScore(570, valorCriterioB)
    score1CriterioC = obterValorDoScore(170, valorCriterioC)

    score2CriterioA = obterValorDoScore(620, valorCriterioA)
    score2CriterioB = obterValorDoScore(190, valorCriterioB)
    score2CriterioC = obterValorDoScore(190, valorCriterioC)

    somaDosScoresAntigo = somarScore(score1CriterioA, score1CriterioB, score1CriterioC)
    somaDosScoresNovo = somarScore(score2CriterioA, score2CriterioB, score2CriterioC)

    classificacaoScoreAntigo = classificarScoreAntigo(somaDosScoresAntigo)
    classificacaoScoreNovo = classificarScoreNovo(somaDosScoresNovo)

    print('-=' * 20)
    print(f'Score 1.0: {somaDosScoresAntigo} - {classificacaoScoreAntigo}')
    print(f'Score 2.0: {somaDosScoresNovo} - {classificacaoScoreNovo}')
    print('-=' * 20)  

main()    



