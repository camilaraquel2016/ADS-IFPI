from utils import obterNumRealPositivo

def obter_percentual(salario_atual):
    if salario_atual < 3000:
        return 0.25
    elif salario_atual < 6000:
        return 0.2
    elif salario_atual < 10000:
        return 0.15
    else:
        return 0.1
    

def calcular_aumento(valor_base, percentual):
    return percentual * valor_base


def saida(soma_salarios_atuais, soma_salarios_reajustados):
    return f'''
    Soma dos salários atuais: R${soma_salarios_atuais:.2f}
    Soma dos salarios reajustados: R${soma_salarios_reajustados:.2f}
    Diferença entre os salários atuais e reajustados: R${soma_salarios_reajustados - soma_salarios_atuais:.2f}'''


def calcular_salarios(soma_salarios_atuais = 0, soma_salarios_reajustados = 0):
    salario = obterNumRealPositivo('Salário: (flag = 0) ')

    if salario != 0:

        percentual_aumento = obter_percentual(salario)
        aumento = calcular_aumento(salario, percentual_aumento)
        salario_reajustado = salario + aumento
        print(f'Salário reajustado: R${salario_reajustado:.2f}')

        soma_salarios_atuais += salario
        soma_salarios_reajustados += salario_reajustado
        return calcular_salarios(soma_salarios_atuais, soma_salarios_reajustados)
    
    return saida(soma_salarios_atuais, soma_salarios_reajustados)


def main():
    print(calcular_salarios(0, 0))

main()    