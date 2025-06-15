from utils import obterNumRealLimiteMin, obterNumInteiroNaFaixa, obterNumReal
#11:06


# menu das taxas

# pedir num de parcleas, min 2 e max 24x
# valor min de emprestimo  salario mi
# declara na main o salrio mi
# valor maximo da parcela é 40% doa renda


def calcularIOF(valorDoEmprestimo, qtdParcelas):
    qtdDias = qtdParcelas * 30
    iofFixo = (0.38 / 100) * valorDoEmprestimo
    iofDiario = (0.0082 / 100) * qtdDias * valorDoEmprestimo
    return iofFixo + iofDiario



def calcularTaxaDeJuros(qtdParcelas, taxaSelic):
    if qtdParcelas <= 6:
        return (50 / 100) * taxaSelic
    elif qtdParcelas < 12:
        return (75 / 100) * taxaSelic
    elif qtdParcelas <= 18:
        return (100 / 100) * taxaSelic
    else:
        return (130 / 100) * taxaSelic 
    

def calcularMontante(capital, taxa, tempo):
    return capital * ( 1 + taxa) ** tempo


def obterSituacao(comprometimentoDaRenda):
    return 'APROVADO' if comprometimentoDaRenda <= 0.4 else 'NEGADO'


def apresentarSaida(valorDoEmprestimo, valorDoIOF, juros, montante, qtdParcelas, valorDaParcela, comprometimentoDaRenda, situacaoDoEmprestimo):
    print(f'''
    Valor Pedido: R${valorDoEmprestimo:.2f}
    Valor do IOF: R${valorDoIOF:.2f}
    Valor dos Juros a pagar: R${juros:.2f}
    Valor Total a pagar: R${montante:.2f}
    Valor da Parcela Mensal: {qtdParcelas}x de R${valorDaParcela:.2f}
    Comprometimento da Renda Mensal: {comprometimentoDaRenda:.1f}%
    Empréstimo {situacaoDoEmprestimo}
    ''')

def main():
    salarioMinimo = 1518
    taxaSelic = 13.75 / 100
    rendaMensal = obterNumReal('Renda mensal: R$')
    valorDoEmprestimo = obterNumRealLimiteMin('Valor do empréstimo: R$', salarioMinimo)
    qtdParcelas = obterNumInteiroNaFaixa('Quantidade de parcelas: ', 2, 24)

    valorDoIOF = calcularIOF(valorDoEmprestimo, qtdParcelas)
    valorComIOF = valorDoEmprestimo + valorDoIOF
    percentualTaxa = calcularTaxaDeJuros(qtdParcelas, taxaSelic)
    montante = calcularMontante(valorComIOF, percentualTaxa, qtdParcelas)
    juros = montante - valorDoEmprestimo
    valorDaParcela = montante / qtdParcelas
    comprometimentoDaRenda = valorDaParcela / rendaMensal

    situacaoDoEmprestimo = obterSituacao(comprometimentoDaRenda)    

    apresentarSaida(valorDoEmprestimo, valorDoIOF, juros, montante, qtdParcelas, valorDaParcela, comprometimentoDaRenda, situacaoDoEmprestimo)    

   
main()   

    





