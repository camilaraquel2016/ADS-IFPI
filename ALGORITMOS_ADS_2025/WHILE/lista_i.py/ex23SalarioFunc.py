def calcularSalario(valorDaHora, valorPorDependente, descontoINSS, descontoIR):
    resposta = 1

    while resposta == 1:
        codFunc = int(input('Código do funcionário: '))
        horasTrabalhadas = int(input('Horas trabalhadas por esse funcionário: '))
        numDependentes = int(input('Número de dependentes: '))

        salarioBruto = horasTrabalhadas * valorDaHora + numDependentes * valorPorDependente


        valorDescontoINSS = descontoINSS * salarioBruto
        valorDescontoIR = descontoIR * salarioBruto

        descontosTotais = valorDescontoINSS + valorDescontoIR

        salarioLiquido = salarioBruto - descontosTotais

        print('-=' * 10)
        print(f'Código do funcionário: {codFunc}\nValor descontado para INSS: R${valorDescontoINSS:.2F}\nValor descontado Para IR: R${valorDescontoIR:.2f}\nSalário líquido: R${salarioLiquido:.2f}')
    
        resposta = int(input('Digite 1 para continuar ou qualquer número para sair: '))


def main():
    valorDaHora = 12
    valorPorDependente = 40
    descontoINSS = 8.5 / 100
    descontoIR = 5 / 100

    calcularSalario(valorDaHora, valorPorDependente, descontoINSS, descontoIR)
    print('Encerrando programa...')

main()