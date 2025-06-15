from itertools import count

def obter_dias_necessarios(populacao_cidade_a, populacao_cidade_b, taxa_anual_cidade_a, taxa_anual_cidade_b):

    for ano in count():
        if populacao_cidade_a > populacao_cidade_b:
            return ano + 1
        
        populacao_cidade_a += (taxa_anual_cidade_a * populacao_cidade_a)
        populacao_cidade_b += (taxa_anual_cidade_b * populacao_cidade_b)
        

def main():
    populacao_cidade_a = 200000
    populacao_cidade_b = 800000

    taxa_anual_cidade_a = 3.5 / 100
    taxa_anual_cidade_b = 1.35 / 100

    qtd_dias = obter_dias_necessarios(populacao_cidade_a, populacao_cidade_b, taxa_anual_cidade_a, taxa_anual_cidade_b)

    print(f'Será necessário {qtd_dias} dias para que a cidade A ultrapasse a cidade B em relação ao número de habitantes')

main()    