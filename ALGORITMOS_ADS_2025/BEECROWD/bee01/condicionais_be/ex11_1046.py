def obter_duracao_em_horas(hora_inicio, hora_fim):
    return hora_fim - hora_inicio if hora_fim > hora_inicio else hora_fim - hora_inicio + 24


def main():
    valores_das_horas = input().split()

    hora_inicio = int(valores_das_horas[0])
    horas_fim = int(valores_das_horas[1])

    duracao_em_horas = obter_duracao_em_horas(hora_inicio, horas_fim)

    print(f'O JOGO DUROU {duracao_em_horas} HORA(S)') 

main()    