from utils import obterNumRealLimiteMin, obterNumReal

def calcularValorTarifado(consumoKWh):
    return 0 if consumoKWh <= 30 else 0.59 * consumoKWh if consumoKWh <= 100 else 0.75 * consumoKWh


def calcularICMS(valorTarifado):
    return 0.25 * valorTarifado


def calcularCONFIS(valorTarifado):
    return 0.15 * valorTarifado


def calcularTaxaDeIluminacao(consumo, valorTarifado):
    return 0.06 * valorTarifado if consumo > 80 else 0


def calcularQtdBandeiras(consumo):
    qtdBandeira = consumo // 100
    if consumo % 100 != 0:
        qtdBandeira += 1
    return qtdBandeira    
    

def main():
    taxaDaBandeira = 8

    leituraAnterior = obterNumReal('Leitura (anterior) em KWh : ')
    leituraAtual = obterNumRealLimiteMin('Leitura (atual) em KWh : ', leituraAnterior + 1)
 
    consumo = leituraAtual - leituraAnterior

    valorTarifado = calcularValorTarifado(consumo)
    qtdBandeiras = calcularQtdBandeiras(consumo)
    valorDaBandeira = taxaDaBandeira * qtdBandeiras
    valorDoCONFIS = calcularCONFIS(valorTarifado)
    valorDoICMS = calcularICMS(valorTarifado)
    taxaDeIluminacao = calcularTaxaDeIluminacao(consumo, valorTarifado)
    
    print(f'''
    Consumo: {consumo:.1f} KWh
    Valor Faturado R${valorTarifado:.2f}
    Bandeira R${valorDaBandeira:.2f} ({qtdBandeiras:.0f} bandeiras)
    ICMS R${valorDoICMS:.2f}
    PIS/CONFIS R${valorDoCONFIS:.2f}
    Taxa Iluminação R${taxaDeIluminacao:.2f}
    ''')

main()






