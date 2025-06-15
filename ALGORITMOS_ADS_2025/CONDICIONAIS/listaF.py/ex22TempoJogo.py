from utils import entradaInt, validarNumLimiteInt

def calcularTempo(horaInicio, minutosInicio, horaFim, minutosFim):
    tempoInicioEmMinutos = horaInicio * 60 + minutosInicio
    tempoFimEmMinutos = horaFim * 60 + minutosFim

    if tempoFimEmMinutos > tempoInicioEmMinutos:
        tempoEmMinutos = tempoFimEmMinutos - tempoInicioEmMinutos
    elif tempoFimEmMinutos < tempoInicioEmMinutos:
        tempoEmMinutos = tempoFimEmMinutos + 1440 - tempoInicioEmMinutos
    else:
        tempoEmMinutos = 1440 

    horas = tempoEmMinutos // 60
    minutos = tempoEmMinutos % 60

    if horas != 0:
        if minutos != 0:
            return f'{horas} hora(s) e {minutos} minuto(s)'
        else:
            return f'{horas} horas(s)'
    else:
        return f'{minutos} minuto(s)'
    

def main():
    print('-=-INÍCIO DO JOGO-=-')

    horaInicio = entradaInt('Hora início: ')
    horaInicio = validarNumLimiteInt(horaInicio, 0, 23, 'Horas início: ')

    minutosInicio = entradaInt('Minutos início: ')
    minutosInicio = validarNumLimiteInt(minutosInicio, 0, 59, 'Minutos início: ')

    print('-=-FIM DO JOGO-=-')
    horaFim = entradaInt('Hora Fim: ')
    horaFim = validarNumLimiteInt(horaFim, 0, 23, 'Hora Fim: ')

    minutosFim = entradaInt('Minutos fim: ')
    minutosFim = validarNumLimiteInt(minutosFim, 0, 59, 'Minutos fim: ')

    tempo = calcularTempo(horaInicio, minutosInicio, horaFim, minutosFim)

    print(f'O jogo teve uma duração de {tempo}')

main()    

    



   

