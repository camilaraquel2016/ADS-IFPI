def obter_percentual_de_aumento(salario_atual):
    if salario_atual <= 400:
        return 0.15
    elif salario_atual <= 800:
        return 0.12
    elif salario_atual <= 1200:
        return 0.1
    elif salario_atual <= 2000:
        return 0.07
    else:
        return 0.04
    

def calcular_aumento(salario_atual, percentual):
    return percentual * salario_atual


def main():
    salario_atual = float(input())
    percentual = obter_percentual_de_aumento(salario_atual)
    aumento = calcular_aumento(salario_atual, percentual)
    novo_salario = salario_atual + aumento

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {aumento:.2f}')
    print(f'Em percentual: {percentual * 100:.0f} %')

main()    


