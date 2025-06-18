# questão que pode ser feita usando While em algumas partes, entretanto será usado o FOR para fins de prática do uso dessa estrutura de repetição.
# será usado o for com o auxílio da função count do módulo itertools.

from itertools import count 

def calcular_retorno_no_ano(taxa_juros_mes, valor_investido_mes, montante_atual):

    for mes in range(12):
        montante_atual += (taxa_juros_mes * montante_atual) 
        montante_atual += valor_investido_mes
    
    return montante_atual


def repetir_ate_parar(taxa_juros_mes, valor_investido_mes, montante_atual):
    retorno_financeiro = montante_atual
    
    for repeticao in count(1):
        
        retorno_financeiro = calcular_retorno_no_ano(taxa_juros_mes, valor_investido_mes, retorno_financeiro)

        print(f'Atualmente seu montante está com o valor total de R${retorno_financeiro:.2f}')
        resposta = input('Deseja continuar? (S/N) ')

        if resposta == 'N':
            return retorno_financeiro, repeticao


def main():
    montante_atual = 0
    taxa_juros_mes = 1 / 100
    valor_investido_mes = 100

    resultado = repetir_ate_parar(taxa_juros_mes, valor_investido_mes, montante_atual)

    retorno_finaceiro = resultado[0]
    qtd_anos = resultado[1]

    print(f'Após {qtd_anos} anos, o seu dinheiro atingiu um valor total de R${retorno_finaceiro:.2f}')

main()
    







    




