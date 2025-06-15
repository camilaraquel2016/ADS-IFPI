from itertools import count
from utils import obter_real_positivo

def obter_percentual(salario_atual):
    if salario_atual <= 2999.99:
        return 0.25
    elif salario_atual <= 5999.99:
        return 0.2
    elif salario_atual <= 9999.99:
        return 0.15
    else:
        return 0.1


def obter_aumento(percentual, valor):
    return percentual * valor


def saida_final(tot_sal_atuais, tot_sal_ajustados):
    diferenca = tot_sal_ajustados - tot_sal_atuais

    return f'''
    Soma dos salários atuais: R${tot_sal_atuais:.2f}
    Soma dos salários ajustados: R${tot_sal_ajustados:.2f}
    Diferença das somas: R${diferenca:.2f}
'''


def gerenciar_salarios():
    soma_sal_atuais = 0
    soma_sal_ajustados = 0

    for func in count():
        print(f'-=-ANÁLISE DO {func + 1}° FUNCIONÁRIO-=-')
        salario_atual = obter_real_positivo('Salário atual: (flag = 0) R$')

        if salario_atual == 0:
            return saida_final(soma_sal_atuais, soma_sal_ajustados)

        percentual_de_aumento = obter_percentual(salario_atual)
        aumento = obter_aumento(percentual_de_aumento, salario_atual)
        salario_reajustado = salario_atual + aumento

        soma_sal_atuais += salario_atual
        soma_sal_ajustados += salario_reajustado
      
        print(f'Novo salário: R${salario_reajustado:.2f}')
        
def main():
    resultado = gerenciar_salarios()
    print(resultado)
 
main()
        

        
