def obter_qtd_anos_necessarios(qtd_populacao_a, qtd_populacao_b, percentual_crescimento_pop_a, percentual_crescimento_pop_b, qtd_anos = 0):
    if qtd_populacao_a > qtd_populacao_b:
        return qtd_anos
    
    qtd_populacao_a += percentual_crescimento_pop_a * qtd_populacao_a
    qtd_populacao_b += percentual_crescimento_pop_b * qtd_populacao_b

    qtd_anos += 1
    return obter_qtd_anos_necessarios(qtd_populacao_a, qtd_populacao_b, percentual_crescimento_pop_a, percentual_crescimento_pop_b, qtd_anos)

def main():
    qtd_populacao_a = 200000
    qtd_populacao_b = 800000
    percentual_crescimento_pop_a = 3.5 / 100
    percentual_crescimento_pop_b = 1.35 / 100
    qtd_anos_necessarios = obter_qtd_anos_necessarios(qtd_populacao_a, qtd_populacao_b, percentual_crescimento_pop_a, percentual_crescimento_pop_b, 0)
    print(f'Para a população A ultrapassar a populção B são necessários {qtd_anos_necessarios} anos')

main()    

    