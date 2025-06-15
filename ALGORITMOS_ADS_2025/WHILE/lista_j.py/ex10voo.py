from utils import obterNumInt, obterNumReal

def converterLitroParaKg(litros):
    return litros * 1.5


def converterKgParaLitros(kg):
    return kg / 1.5


def pesoDosPassageirosEBagagens(pesoDeCadaPassageiro, pesoDeCadaBagagem):
    qtdPassageiros = 0
    qtdBagagemTotal = 0
    bilhete = obterNumInt('N° do bilhete: (flag = 0) ')

    while bilhete != 0:
        qtdPassageiros += 1
        qtdBagagem = obterNumInt('Quantidade de bagagem: ')
        qtdBagagemTotal += qtdBagagem
        bilhete = obterNumInt('N° do bilhete: (flag = 0) ')

    pesoTotalPassageiro = qtdPassageiros * pesoDeCadaPassageiro
    pesoTotalBagagem = qtdBagagemTotal * pesoDeCadaBagagem
    return pesoTotalPassageiro + pesoTotalBagagem


def pesoDaCarga(qtdContainer):
    contador = 1
    pesoTotalContainer = 0

    while contador <= qtdContainer:
        pesoDoContainer = obterNumReal(f'Peso do {contador}° container: (Kg) ')
        pesoTotalContainer += pesoDoContainer
        contador += 1
    return pesoTotalContainer


def podeLevantarVoo(pesoMinDeCombustivel, pesoPossivelCombustivel):
    return pesoPossivelCombustivel >= pesoMinDeCombustivel


def obterQtdLitrosCombustivel(pesoPossivelCombustivel, litrosMinCombustivel):
    qtdLitrosAceita = converterKgParaLitros(pesoPossivelCombustivel)
    while True:
        litrosDeCombustivel = obterNumReal('Quantidade de combustível: (litros) ')
        if litrosDeCombustivel >= litrosMinCombustivel and litrosDeCombustivel <= qtdLitrosAceita:
            return litrosDeCombustivel
        else:
            print(f'Quantidade de litros de combustível inválida!\nA quantidade deve ser maior ou igual a {litrosMinCombustivel} e menor ou igual a {qtdLitrosAceita:.2f}')


def main():
    pesoDeDecolagem = 500000
    litrosMinCombustivel = 10000
    pesoMinCombustivel = converterLitroParaKg(litrosMinCombustivel)
    pesoDeCadaPassageiro = 70
    pesoDeCadaBagagem = 10
    qtdContainer = obterNumInt('Quantidade de container: ')
    pesoTotalCargaContainer = pesoDaCarga(qtdContainer)
    pesoTotalPassageiro = pesoDosPassageirosEBagagens(pesoDeCadaPassageiro, pesoDeCadaBagagem)
    pesoPossivelCombustivel = pesoDeDecolagem - (pesoTotalCargaContainer + pesoTotalPassageiro) 

    if podeLevantarVoo(pesoMinCombustivel, pesoPossivelCombustivel):
        qtdDeCombustivel = obterQtdLitrosCombustivel(pesoPossivelCombustivel, litrosMinCombustivel)
        print('Pode levantar vôo')
    else:
        print('Não é possível levantar vôo')    

main()     






    



     




















    







# def main():
#     pesoDeDecolagemPadrao = 500000

