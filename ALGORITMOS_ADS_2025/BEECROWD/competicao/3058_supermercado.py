def obter_menor_valor_da_grama(qtd_supermercados):
    menor_valor_da_grama = float('inf')

    for supermercado in range(qtd_supermercados):
        valor_e_qtd_gramas = input().split()
        valor = float(valor_e_qtd_gramas[0])
        qtd_gramas = int(valor_e_qtd_gramas[1])
        valor_da_grama = valor / qtd_gramas

        if valor_da_grama < menor_valor_da_grama:
            menor_valor_da_grama = valor_da_grama

    return menor_valor_da_grama    

        
def main():
    qtd_supermercados = int(input())
    menor_valor_da_grama = obter_menor_valor_da_grama(qtd_supermercados)
    menor_valor_a_pagar_no_kg = menor_valor_da_grama * 1000
    print(f'{menor_valor_a_pagar_no_kg:.2f}')

main()

