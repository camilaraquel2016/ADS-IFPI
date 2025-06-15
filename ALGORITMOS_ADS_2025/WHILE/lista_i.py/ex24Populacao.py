def apresentarDados():
    resposta = 1
    qtdHabitantes = 0
    numFilhosTotais = 0
    salarioAte1000 = 0
    somaSalario = 0

    while resposta == 1:
        salario = float(input('Salário: R$'))
        somaSalario += salario
        if salario <= 1000:
            salarioAte1000 += 1
        numFilhos = int(input('Número de filhos: '))
        numFilhosTotais += numFilhos
        qtdHabitantes += 1
        resposta = int(input('Digite 1 para continuar ou qualquer número para sair: '))
        


    mediaDeSalario = somaSalario / qtdHabitantes
    mediaNumFilhos = numFilhosTotais / qtdHabitantes
    percentualSalarioAte1000 = salarioAte1000 / qtdHabitantes * 100
    

    return f'-=-=--=-DADOS-=-=-=-=-\nMédia de salário da população: R${mediaDeSalario:.2f}\nMédia do número de filhos: {mediaNumFilhos}\nPercentual de pessoas com salário de até R$1000: {percentualSalarioAte1000}'


def main():
    print(apresentarDados())

main()    

        
