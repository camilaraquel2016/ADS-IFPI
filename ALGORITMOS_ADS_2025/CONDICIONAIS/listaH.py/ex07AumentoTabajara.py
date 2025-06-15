def calcularReajustes(salario):
    if salario <= 280:
        percentualAumento = 0.2
    elif salario < 700:
        percentualAumento = 0.15
    elif salario < 1500:
        percentualAumento = 0.1
    else:
        percentualAumento = 0.05

    aumento = salario * percentualAumento
    novoSalario = salario + aumento    

    return f'Salário antes do reajuste: R${salario:.2f}\nPercentual de aumento aplicado: {percentualAumento * 100}%\nValor do aumento: R${aumento:.2f}\nNovo salário: R${novoSalario:.2f}'


        

def main():
    salario = float(input('Qual seu salário? R$'))

    print(calcularReajustes(salario))

main()