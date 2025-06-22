from utils import obter_inteiro_maior_que_0, obterNumInteiroPositivo

def calcular_salario_bruto(valor_por_hora, valor_por_dependente, qtd_horas_trabalhadas, qtd_dependentes):
    return (valor_por_hora * qtd_horas_trabalhadas) + (valor_por_dependente * qtd_dependentes)


def calcular_desconto(percentual, salario_bruto):
    return percentual * salario_bruto


def saida(salario_liquido, desconto_inss, desconto_ir):
    return f'''
    -=-=-=-=-RESUMO-=-=-=-=-
    Desconto INSS: R${desconto_inss:.2f} 
    Desconto IR: R${desconto_ir:.2f}
    Salário líquido: R${salario_liquido:.2f}
'''
    
    
def calcular_salarios(qtd_func, valor_por_hora, valor_por_dependente, taxa_inss, taxa_ir, contador = 1):

    if contador <= qtd_func:
        print(f'-=-Salário {contador}° funcionário-=-')
        cod_func = obter_inteiro_maior_que_0('Código funcionário: ')
        qtd_horas_trabalhadas = obterNumInteiroPositivo('Quantidade de horas trabalhadas: ')
        qtd_dependentes = obterNumInteiroPositivo(f'Quantidade de dependentes: ')

        salario_bruto = calcular_salario_bruto(valor_por_hora, valor_por_dependente, qtd_horas_trabalhadas, qtd_dependentes)
        desconto_inss = calcular_desconto(taxa_inss, salario_bruto)
        desconto_ir = calcular_desconto(taxa_ir, salario_bruto)
        salario_liquido = salario_bruto - (desconto_inss + desconto_ir)

        print(saida(salario_liquido, desconto_inss, desconto_ir))
        print()
        return calcular_salarios(qtd_func, valor_por_hora, valor_por_dependente, taxa_inss, taxa_ir, contador + 1)
    
    return f'Cálculos de salários concluídos...'


def main():
    valor_por_hora = 12
    valor_por_dependente = 40
    taxa_inss = 8.5 / 100
    taxa_ir = 5 / 100
    qtd_func = obter_inteiro_maior_que_0('Quantidade de funcionários: ')
    print(calcular_salarios(qtd_func, valor_por_hora, valor_por_dependente, taxa_inss, taxa_ir, 1))

main()