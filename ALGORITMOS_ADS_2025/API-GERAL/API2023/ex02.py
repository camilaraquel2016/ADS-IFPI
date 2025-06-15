def calcularCapacidadeEmlitros(largura, comprimento, profundidade): # recebe as medidas em cm e retorna o valor da capacidade em litros
    return (largura * comprimento * profundidade) / 1000


def calcularCapacidadeMaxima(capacidadeNormal): # calcula qual valor recomendado para encher uma piscina, no caso 85% da sua capacidade normal
    return 0.85 * capacidadeNormal


def obterQtdLitrosAproximado(qtdLitros): # arredonda a quantidade de litros para o próximo múltiplo de 1000, ex: 1001, arredonda para 2000 e se for 1000 continua o mesmo 1000
    qtdMilhar = qtdLitros // 1000
    resto = qtdLitros % 1000
    
    if resto >= 1:
        qtdMilhar += 1
    
    return qtdMilhar * 1000
    

def calcularValorParaEncher(qtdLitros, valorPor1000Litros): # valor gasto para encher a piscina de acordo com sua capacidade máxima
    return (qtdLitros / 1000) * valorPor1000Litros


def calcularManutencao(capacidadeMaxima, valorPor1000Litros): # valor gasto todo mês para a piscina manter o mesmo nível de água, 10% da capacidade máxima
    qtdLitrosParaRepor = 0.10 * capacidadeMaxima
    qtdLitrosParaRepor = obterQtdLitrosAproximado(qtdLitrosParaRepor)
    return (qtdLitrosParaRepor / 1000) * valorPor1000Litros


def main():
    larguraDaPiscina = float(input('Largura da piscina: (cm) '))
    comprimentoDaPiscina = float(input('Comprimento da piscina: (cm) '))
    profundidadeDaPiscina = float(input('Profundidade da piscina: (cm) '))
    valorPor1000litros = float(input('Valor cobrado a cada 1000 litros de água: R$ '))
    
    capacidadeLitros = calcularCapacidadeEmlitros(larguraDaPiscina, comprimentoDaPiscina, profundidadeDaPiscina)
 
    capacidadeMaxima = calcularCapacidadeMaxima(capacidadeLitros)
 
    qtdLitros = obterQtdLitrosAproximado(capacidadeMaxima)

    valorGastoParaEncher = calcularValorParaEncher(qtdLitros, valorPor1000litros)

    valorReporMensalmente = calcularManutencao(capacidadeMaxima, valorPor1000litros)

    print('-=' * 20)

    print(f'Capacidade recomendada para encher a piscina: {capacidadeMaxima:.1f} litros')
    print(f'Gasto para encher a piscina: R${valorGastoParaEncher:.2f}')
    print(f'Valor para repor mensalmente a água perdida por evaporação: R${valorReporMensalmente:.2f}')
    
main()
