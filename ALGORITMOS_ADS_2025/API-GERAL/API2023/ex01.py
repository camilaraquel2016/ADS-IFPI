def obterPerentualCashback(valorDaCompra):
    if valorDaCompra <= 250:
        return 0.05
    elif valorDaCompra < 500:
        return 0.07
    elif valorDaCompra <= 750:
        return 0.08
    else:
        valorDeDesconto = (750 * 0.08) + (valorDaCompra - 750) * 0.25
        percentual = valorDeDesconto / valorDaCompra
        return percentual
    

def calcularDesconto(percentual, valor):
    return percentual * valor


def saida(faturamentoVendas, somaDosCashback, valorTotalDeDesconto, maiorValorDeCashback, menorValorDeCashback, valorMedioCashback):
    return f'''
            Faturamento Total: R${faturamentoVendas:.2f}
            Cashback totais: {somaDosCashback:.1f}%
            Valor investido em cashback: R${valorTotalDeDesconto:.2f}
            Maior valor pago em cashback: R${maiorValorDeCashback:.2f}
            Menor valor pago em cashback: R${menorValorDeCashback:.2f}
            Valor médio pago em cashback: R${valorMedioCashback:.2f}'''


def gerenciarLoja(numClientes):
    maiorValorDeCashback = 0
    menorValorDeCashback = 100000000000
    contador = 1
    faturamentoVendas = 0
    valorTotalDeDesconto = 0
    somaDosCashback = 0

    while contador <= numClientes:
        contador += 1
        nomeCliente = str(input('Nome da cliente: '))

        valorDasCompras = float(input('Valor das compras: R$'))
        faturamentoVendas += valorDasCompras

        percentualCashback = obterPerentualCashback(valorDasCompras)
        somaDosCashback += percentualCashback * 100 

        desconto = calcularDesconto(percentualCashback, valorDasCompras)
        valorTotalDeDesconto += desconto

        if desconto > maiorValorDeCashback:
            maiorValorDeCashback = desconto
        if desconto < menorValorDeCashback:
            menorValorDeCashback =  desconto
        
        valorMedioCashback = valorTotalDeDesconto / numClientes

        print(f'Você recebeu {percentualCashback * 100:.1F}% de cashback, ou seja, R${desconto:.2f} de desconto')

    return saida(faturamentoVendas, somaDosCashback, valorTotalDeDesconto, maiorValorDeCashback, menorValorDeCashback, valorMedioCashback)
       

def main():
    print('-=-LOJA VOCÊ É ESPECIAL-=-')
    quantClientes = int(input('Número de clientes: '))
    print(gerenciarLoja(quantClientes))

main()    