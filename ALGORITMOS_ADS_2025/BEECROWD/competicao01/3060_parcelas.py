def obter_quociente(dividendo, divisor):
    return dividendo // divisor

def obter_resto(dividendo, divisor):
    return dividendo % divisor


def obter_parcelas(valor_da_compra, qtd_parcelas):
    parcela_base = obter_quociente(valor_da_compra, qtd_parcelas)
    valor_restante_a_pagar_das_parcelas = obter_resto(valor_da_compra, qtd_parcelas) 

    parcelas = []

    for i in range(qtd_parcelas):
        if valor_restante_a_pagar_das_parcelas > 0:
            parcela = parcela_base + 1    
            valor_restante_a_pagar_das_parcelas -= 1
        else:
            parcela = parcela_base   

        parcelas.append(parcela)

    return parcelas        


def exibir_parcelas(parcelas):
    for parcela in parcelas:
        print(parcela)


def main():
    valor_da_compra = int(input())
    qtd_parcelas = int(input())
    parcelas = obter_parcelas(valor_da_compra, qtd_parcelas)
    exibir_parcelas(parcelas)

main()    

    
