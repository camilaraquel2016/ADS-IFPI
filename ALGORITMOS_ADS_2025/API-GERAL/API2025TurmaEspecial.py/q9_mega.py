#início 25/05 - 14:30
# fim 2505 - 15:07
from utils import obterNumRealPositivo, obterNumReal

def main():
    valorDoPremio = obterNumRealPositivo('Valor do prêmio: R$')
    taxaImposto = 20
    print(repartirPremio(valorDoPremio, taxaImposto))


def repartirPremio(valorDoPremio, taxaImposto):
    totalDeColaboracao = 0
    qtdPessoas = 0
    contador = 1 
    maiorInvestimento = 0
    menorInvestimento = 100000000000000

    while True:
        label = f'Valor investido pela {contador}° pessoa: (flag = 0) R$'
        valorDaColaboracao = obterNumReal(label)

        if valorDaColaboracao == 0:
            break

        totalDeColaboracao += valorDaColaboracao
        contador += 1
        qtdPessoas += 1

        if valorDaColaboracao > maiorInvestimento:
            maiorInvestimento = valorDaColaboracao
        if valorDaColaboracao < menorInvestimento:
            menorInvestimento = valorDaColaboracao
    if qtdPessoas == 0:
        return f'Nenhuma colaboração cadastrada!'
    else:
        resultado = exibirResultado(valorDoPremio, taxaImposto, totalDeColaboracao, maiorInvestimento, menorInvestimento)
        return resultado    
    

def exibirResultado(valorDoPremio, taxaDoImposto, totalColaboracao, maiorColaboracao, menorColaboracao):
    valorDoImposto = taxaDoImposto / 100 * valorDoPremio
    valorFinalDoPremio = valorDoPremio - valorDoImposto

    maiorPremio = (maiorColaboracao / totalColaboracao) * valorFinalDoPremio
    menorPremio = (menorColaboracao / totalColaboracao) * valorFinalDoPremio

    return  f'''
    Valor do prêmio: R${valorDoPremio:.2f}
    Valor do imposto: R${valorDoImposto:.2f}
    Valor final do prêmio: R${valorFinalDoPremio:.2f}
    Maior prêmio: R${maiorPremio:.2f}
    Menor prêmio: R${menorPremio:.2f}
'''


main()







