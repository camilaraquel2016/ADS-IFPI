def obter_valor_do_imposto(salario):
    imposto_total = 0

    if salario > 4500:
        parcela_do_valor = salario - 4500
        imposto_total += 0.28 * parcela_do_valor
        salario -= parcela_do_valor

    if salario > 3000:
        parcela_do_valor = salario - 3000
        imposto_total += 0.18 * parcela_do_valor
        salario -= parcela_do_valor

    if salario > 2000:
        parcela_do_valor = salario - 2000
        imposto_total += 0.08 * parcela_do_valor
        salario -= parcela_do_valor

    return imposto_total


def main():
    salario = float(input())
    imposto_a_ser_pago = obter_valor_do_imposto(salario)

    if imposto_a_ser_pago > 0:
        print(f'R$ {imposto_a_ser_pago:.2f}')
    else:
        print('Isento')    

main()        

