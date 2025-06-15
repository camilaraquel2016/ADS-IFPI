def obterPercentualIR(salario):
    if salario <= 900:
        return 0
    elif salario <= 1500:
        return 0.05
    elif salario <= 2500:
        return 0.1
    else:
        return 0.2
    

def calcularDesconto(valor, taxa):
    return taxa * valor


def main():
    valorHora = float(input('Qual valor da hora trabalhada? R$'))
    qtdHoras = int(input('Quantas horas foram trabalhadas no mês? '))
    salarioBruto = valorHora * qtdHoras
    percentualDoIR = obterPercentualIR(salarioBruto)

    valorDoIR = calcularDesconto(salarioBruto, percentualDoIR)
    valorDoINSS = calcularDesconto(salarioBruto, 0.1)
    valorDoFGTS = calcularDesconto(salarioBruto, 0.11)

    totalDesconto = valorDoIR + valorDoINSS

    salarioLiquido = salarioBruto - totalDesconto

    print(f'Salário Bruto: ({valorHora} * {qtdHoras}): R${salarioBruto:.2f}')
    print(f'(-) IR ({percentualDoIR * 100}%): R${valorDoIR:.2f}')
    print(f'(-) INSS (10%): {valorDoINSS:.2f}')
    print(f'FGTS (11%): R${valorDoFGTS:.2f}')
    print(f'Total de descontos: R${totalDesconto:.2f}')
    print(f'Salário líquido: R${salarioLiquido:.2f}')

main()