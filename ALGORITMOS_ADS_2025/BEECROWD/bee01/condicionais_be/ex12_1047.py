def obter_duracao_jogo(horas_inicio, minutos_inicio, horas_fim, minutos_fim):
    tempo_total_inicio = horas_inicio * 60 + minutos_inicio
    tempo_total_fim = horas_fim * 60 + minutos_fim
    if tempo_total_fim > tempo_total_inicio:
        duracao = tempo_total_fim - tempo_total_inicio
    else:
        duracao = tempo_total_fim - tempo_total_inicio + 1440

    horas = duracao // 60
    minutos = duracao % 60

    return horas, minutos     
    

def main():
    valores = input().split()

    hora_inicial = int(valores[0])
    minuto_inicial = int(valores[1])
    hora_final = int(valores[2])
    minuto_final = int(valores[3])

    duracao = obter_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final)

    duracao_hora, duracao_minuto = duracao

    print(f'O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)')

main()    

