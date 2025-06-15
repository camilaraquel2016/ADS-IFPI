from q1_number_utils import obterNumInteiroNaFaixa

# início 25/05 - 13:41
# fim 25/05 - 14:20

def calcularDiasTotais(dia, mes, ano):
    return dia + mes * 30 + ano * 365


def calcularDistancia(n1, n2):
    return n1 - n2 if n1 > n2 else n2 - n1


def formatarSaida(dias, meses, anos):
    if dias == 1:
        diaSaida = '1 dia'
    else:
        diaSaida = f'{dias} dias'

    if meses == 1:
        mesesSaida = '1 mês'
    else:
        mesesSaida = f'{meses} meses'

    
    if anos == 1:
        anosSaida = '1 ano'
    else:
        anosSaida = f'{anos} anos'

    if anos >= 1:
        if meses >= 1:
            if dias >= 1:
                return f'{anosSaida}, {mesesSaida} e {diaSaida}'
            else:
                return f'{anosSaida} e {mesesSaida}'
        else:
            if dias >= 1:
                return f'{anosSaida} e {diaSaida}'
            else:
                return f'{anosSaida}'

    else:
        if meses >= 1:
            if dias >= 1:
                return f'{mesesSaida} e {diaSaida}'
            else:
                return f'{mesesSaida}'
        else:
            return f'{diaSaida}'    

def main():
    print('Primeira data')
    dia1 = obterNumInteiroNaFaixa('Dia: ', 1, 30)
    mes1 = obterNumInteiroNaFaixa('Mês: ', 1, 12)
    ano1 = obterNumInteiroNaFaixa('Ano: ', 1, 3000)

    print('Segunda data')
    dia2 = obterNumInteiroNaFaixa('Dia: ', 1, 30)
    mes2 = obterNumInteiroNaFaixa('Mês: ', 1, 12)
    ano2 = obterNumInteiroNaFaixa('Ano: ', 1, 3000)

    diasTotaisData1 = calcularDiasTotais(dia1, mes1, ano1)
    diasTotaisData2 = calcularDiasTotais(dia2, mes2, ano2)

    diferencaEmDias = calcularDistancia(diasTotaisData1, diasTotaisData2)

    anos = diferencaEmDias // 365
    meses = diferencaEmDias % 365 // 30
    dias = diferencaEmDias % 30
    print('-=-Diferença-=-')
    print(formatarSaida(dias, meses, anos))


main()




