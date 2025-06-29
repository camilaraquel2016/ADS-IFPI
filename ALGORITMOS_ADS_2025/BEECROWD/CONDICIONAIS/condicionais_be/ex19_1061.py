def obter_duracao(dia_inicial, hora_inicial, minuto_inicial, segundo_inicial, dia_final, hora_final, minuto_final, segundo_final):
    qtd_dias = dia_final - dia_inicial

    segundos_total_inicio = hora_inicial * 60 * 60 + minuto_inicial * 60 + segundo_inicial
    segundos_total_fim = hora_final * 60 * 60 + minuto_final * 60 + segundo_final

    if segundos_total_fim < segundos_total_inicio:
        duracao_em_segundos = segundos_total_fim - segundos_total_inicio + 86400
        qtd_dias -= 1
    else:
        duracao_em_segundos = segundos_total_fim - segundos_total_inicio

    qtd_horas = duracao_em_segundos // 3600
    qtd_minutos = duracao_em_segundos % 3600 // 60
    qtd_segundos = duracao_em_segundos % 60

    return qtd_dias, qtd_horas, qtd_minutos, qtd_segundos
        

def main():
    dia_inicial = int(input().split()[1])
    horario_inicial = input().split(' : ')

    dia_final = int(input().split()[1])
    horario_final = input().split(' : ')
    
    hora_inicial = int(horario_inicial[0])
    minuto_inicial = int(horario_inicial[1])
    segundo_inicial = int(horario_inicial[2])

    hora_final = int(horario_final[0])
    minuto_final = int(horario_final[1])
    segundo_final = int(horario_final[2])

    duracao = obter_duracao(dia_inicial, hora_inicial, minuto_inicial, segundo_inicial, dia_final, hora_final, minuto_final, segundo_final)
    qtd_dia, qtd_hora, qtd_minuto, qtd_seg = duracao
    print(f'{qtd_dia} dia(s)\n{qtd_hora} hora(s)\n{qtd_minuto} minuto(s)\n{qtd_seg} segundo(s)')    

main()    



    
    
    
