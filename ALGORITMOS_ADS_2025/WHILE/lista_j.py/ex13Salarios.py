from utils import obterNumReal

def obterPercentualAcrescimo(salarioAtual):
    if salarioAtual < 3000:
        return 0.25
    elif salarioAtual < 6000:
        return 0.2
    elif salarioAtual < 10000:
        return 0.15
    else:
        return 0.1


def calcularSalarioComReajuste(salario):
    percentual = obterPercentualAcrescimo(salario)
    return salario + (salario * percentual)


def controlarReajustes():
    contador = 0
    somaSalariosAtuais = 0
    somaSalariosComReajustes = 0
    salario = salario = obterNumReal('Salário: (flag = 0) ')

    while salario != 0:
        contador += 1
        somaSalariosAtuais += salario

        salarioComReajuste = calcularSalarioComReajuste(salario)
        somaSalariosComReajustes += salarioComReajuste

        print(f'Novo salário: R${salarioComReajuste:.2f}')

        salario = obterNumReal('Salário: (flag = 0) ')

    if contador != 0:
        return f'Soma dos salário atuais: R${somaSalariosAtuais:.2f}\nSoma dos salários reajustados: R${somaSalariosComReajustes}\nDiferença dos salários: {somaSalariosComReajustes} - {somaSalariosAtuais} = {somaSalariosComReajustes - somaSalariosAtuais}' 
    else:
        return f'Nenhum salário cadastrado!'

print(controlarReajustes())

        




