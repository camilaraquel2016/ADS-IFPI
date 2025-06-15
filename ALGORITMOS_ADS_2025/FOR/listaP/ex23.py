def calcular_salario_bruto(horas_trabalhadas, valor_da_hora, qtd_dependentes, valor_por_dependente):
    return (horas_trabalhadas * valor_da_hora) + (qtd_dependentes * valor_por_dependente)


def obter_desconto_inss(taxa_inss, salario_bruto):
    return taxa_inss * salario_bruto


def obter_desconto_ir(taxa_ir, salario_bruto):
    return taxa_ir * salario_bruto


def imprimir_informacoes(desconto_inss, desconto_ir, salario_liquido, cod_func):
    return f'''
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Código funcionário: {cod_func}
    Desconto INSS: R${desconto_inss}
    Desconto IR: R${desconto_ir}
    Salário líquido: R${salario_liquido:.2f}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    '''


def calcular_salarios(qtd_funcionarios, valor_da_hora, valor_por_dependente, taxa_inss, taxa_ir):
    final = qtd_funcionarios + 1

    for funcionario in range(1, final, 1):

        print('-=' * 10)
        cod_func = int(input('Código funcionário: '))
        horas_trabalhadas = int(input('Quantidade de horas trabalhadas: '))
        qtd_dependentes = int(input('Quantidade de dependentes: '))

        salario_bruto = calcular_salario_bruto(horas_trabalhadas, valor_da_hora, qtd_dependentes, valor_por_dependente)   
        desconto_inss = obter_desconto_inss(taxa_inss, salario_bruto)  
        desconto_ir = obter_desconto_ir(taxa_ir, salario_bruto)
        salario_liquido = salario_bruto - desconto_inss - desconto_ir
        print(imprimir_informacoes(desconto_inss, desconto_ir, salario_liquido, cod_func))


def main():
    qtd_funcionarios = int(input('Quantidade de funcionários: '))
    valor_da_hora = 12
    valor_por_dependente = 40
    taxa_inss = 8.5 / 100
    taxa_ir = 5 / 100
    
    calcular_salarios(qtd_funcionarios, valor_da_hora, valor_por_dependente, taxa_inss, taxa_ir)


main()


