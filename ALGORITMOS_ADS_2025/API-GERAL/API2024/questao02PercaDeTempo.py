# visto que é um programa de perda de peso, deve-se analisar somente o peso perdido com treino e não o que a pessoa perde normalmente

def qtdCalPerdidasComTreinoMasc(percentualTransport, percentualEscada, tempoPorDia): # diario
    minutos = tempoPorDia * 60
    minutosNoTransport = percentualTransport * minutos
    minutosNaEscada = percentualEscada * minutos
    gastoCalComTransport = minutosNoTransport / 5 * 100
    gastoCalComEscada = minutosNaEscada / 7 * 100
 
    return gastoCalComTransport + gastoCalComEscada

def qtdCalPerdidasComTreinoFem(percentualTransport, percentualEscada, tempoPorDia): # diario
    minutos = tempoPorDia * 60
    minutosNoTransport = percentualTransport * minutos
    minutosNaEscada = percentualEscada * minutos
    gastoCalComTransport = minutosNoTransport / 6 * 100
    gastoCalComEscada = minutosNaEscada / 8 * 100
    return gastoCalComTransport + gastoCalComEscada


def qtdCalPerdidasNaSemanaFem(percentualTransport, percentualEscada, tempoPorDia, gastoCalFem, qtdVezesNaSemana):
    return qtdCalPerdidasComTreinoFem(percentualTransport, percentualEscada, tempoPorDia) * qtdVezesNaSemana
    

def qtdCalPerdidasNaSemanaMasc(percentualTransport, percentualEscada, tempoPorDia, gastoCalMasc, qtdVezesNaSemana):
    return qtdCalPerdidasComTreinoMasc(percentualTransport, percentualEscada, tempoPorDia) * qtdVezesNaSemana
    

def semanasNecessarias(percentualTransport, percentualEscada, tempoPorDia, gastoCalMasc, gastoCalFem, qtdVezesNaSemana, kgParaPerder, sexo):
    calQueDesejaPerder = kgParaPerder * 7000

    if sexo == 1: # feminino
        calPerdidaNaSemana = qtdCalPerdidasNaSemanaFem(percentualTransport, percentualEscada, tempoPorDia, gastoCalFem, qtdVezesNaSemana)
        return calQueDesejaPerder / calPerdidaNaSemana
    else: # masculino
        calPerdidaNaSemana = qtdCalPerdidasNaSemanaMasc(percentualTransport, percentualEscada, tempoPorDia, gastoCalMasc, qtdVezesNaSemana)
        return calQueDesejaPerder / calPerdidaNaSemana
    

def main():
    quantKgPorCal = 7000

    sexo = int(input('Qual seu sexo? Digite 1 para feminino e qualquer dígito para homem '))
    pesoParaPerder = float(input('Quantos Kg deseja perder? '))
    tempoPorDia = float(input('Quantas horas por dia deseja treinar? '))
    vezesNaSemana = int(input('Quantas vezes na semana irá treinar? '))
    percentualTransport = float(input('Do tempo gasto quantos porcentos irá se dedicado ao treino de Transport? ')) / 100
    percentualEscada = 1 - percentualTransport

    print(semanasNecessarias(percentualTransport, percentualEscada, tempoPorDia, vezesNaSemana, pesoParaPerder, sexo))
    
main()


