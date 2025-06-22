from utils import obterNumRealPositivo

def obter_resposta(label):
    resposta = str(input(label)).upper()

    if resposta == 'S' or resposta == 'N':
        return resposta
    
    print('Resposta inválida!\nTente novamente...')
    return obter_resposta(label)


def repetir(valor_investido_todo_mes, retorno_financeiro, taxa_juros_mensal, contador_anos = 1):
    print(f'Seu dinheiro rendeu no total R${retorno_financeiro:.2f} após {contador_anos} ano(s)')
    resposta = obter_resposta('Deseja investir por mais um ano? (S/N) ')

    if resposta == 'S':
        retorno_financeiro = calcular_retorno_financeiro(valor_investido_todo_mes, taxa_juros_mensal, 1, retorno_financeiro)
        return repetir(valor_investido_todo_mes, retorno_financeiro, taxa_juros_mensal, contador_anos + 1)
    
    return retorno_financeiro


def calcular_retorno_financeiro(valor_investido_todo_mes, taxa_juros_mensal, contador = 1, retorno_financeiro = 0):
    if contador <= 12:
        retorno_financeiro += (taxa_juros_mensal / 100) * retorno_financeiro
        retorno_financeiro += valor_investido_todo_mes
        return calcular_retorno_financeiro(valor_investido_todo_mes, taxa_juros_mensal, contador + 1, retorno_financeiro)
    
    return retorno_financeiro


def main():
    valor_investido_todo_mes = obterNumRealPositivo('Valor que será investido todo mês: ')
    taxa_juros_mensal = obterNumRealPositivo('taxa de juros mensal: (%) ')
    retorno_auxiliar = calcular_retorno_financeiro(valor_investido_todo_mes, taxa_juros_mensal, 1, 0)
    retorno_financeiro = repetir(valor_investido_todo_mes, retorno_auxiliar, taxa_juros_mensal, 1)
    print(f'Muito bem, seu dinheiro rendeu um total de R${retorno_financeiro:.2f}')

main()    
    



















