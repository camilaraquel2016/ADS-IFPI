def obter_qtd_dias(valor_do_emprestimo, valor_abatido_diariamente, juros_diario, qtd_dias = 0):
    if valor_do_emprestimo > 0:
        qtd_dias += 1
        valor_do_emprestimo += juros_diario * valor_do_emprestimo
        valor_do_emprestimo -= valor_abatido_diariamente
        return obter_qtd_dias(valor_do_emprestimo, valor_abatido_diariamente, juros_diario, qtd_dias)
    
    return qtd_dias


def main():
    valor_do_emprestimo = 3000
    valor_abatido_diariamente = 200
    juros_diario = 0.85 / 100
    dias = obter_qtd_dias(valor_do_emprestimo, valor_abatido_diariamente, juros_diario, 0)
    print(f'São necessários {dias} dias para concluir o pagamento desse empréstimo')

main()    