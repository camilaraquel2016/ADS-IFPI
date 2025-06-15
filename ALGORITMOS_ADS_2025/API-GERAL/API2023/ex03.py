from utils import obterNumReal, obterNumRealLimiteMin, obterNumRealLimiteMax, obterNumRealNaFaixa

def calcularMesesNecessarios(montanteFinal, aporte, taxaDeJuros):
    montante = 0
    meses = 0
    
    while montante < montanteFinal:
        montante += aporte
        juros = (taxaDeJuros / 100) * montante
        montante += juros
        meses += 1

    return meses    


def formatarTempo(meses):
    ano = meses // 12
    meses = meses % 12

    if ano == 1:
        tempoAno = '1 ano'
    elif ano > 1:
        tempoAno = f'{ano} anos'

    if meses == 1:
        tempoMes = '1 mês'
    elif meses > 1:
        tempoMes = f'{meses} meses'

    if ano > 0 and meses > 0:
        return f'{tempoAno} e {tempoMes}'
    elif ano > 0:
        return tempoAno
    else:
        return tempoMes 
                   


def main():
    percentualLimiteMax = 29.99

    nome = input('Qual seu nome? ')
    objetivo = input(f'Seja bem-vindo(a), {nome}\nQual seu objetivo com esse investimento? ')
    valorFinalDesejado = obterNumReal('Qual o valor desejado para a realização desse objetivo? R$')
    salario = obterNumRealLimiteMin('Qual seu salário? R$', 1)
    percentualDoInvestimento = obterNumRealLimiteMax('Quantos porcento do seu salário você deseja investir? (%) ', percentualLimiteMax) 
    taxaDeJurosInvestimento = obterNumRealNaFaixa('Qual a taxa de juros mensal desse investimento? ', 0.01, 1) 

    aporte = (percentualDoInvestimento / 100) * salario 

    qtdMesesParaObterValorFinal = calcularMesesNecessarios(valorFinalDesejado, aporte, taxaDeJurosInvestimento)
    
    tempoFormatado = formatarTempo(qtdMesesParaObterValorFinal)
    
    print('-=' * 10)

    print(f'Valor desejado: R${valorFinalDesejado:.2f}\nValor investido todo mês: {aporte:.2f}\nTaxa de juros do investimento: {taxaDeJurosInvestimento:.1f}%\nTempo necessário: {tempoFormatado}')
    
main()





    
   
