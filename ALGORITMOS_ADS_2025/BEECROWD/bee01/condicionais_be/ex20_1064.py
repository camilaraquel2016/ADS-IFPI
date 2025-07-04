def eh_positivo(num):
    return num > 0


def obter_dados(qtd_num):
    soma_dos_num_positivos = 0
    qtd_de_num_positivos = 0

    for entrada in range(qtd_num):
        num = float(input())

        if eh_positivo(num):
            soma_dos_num_positivos += num
            qtd_de_num_positivos += 1

    return soma_dos_num_positivos, qtd_de_num_positivos


def obter_media(total, qtd):
    return total / qtd


def main():
    qtd_num = 6
    dados = obter_dados(6)
    soma_dos_num_positivos, qtd_de_num_positivos = dados

    media = obter_media(soma_dos_num_positivos, qtd_de_num_positivos)

    print(f'{qtd_de_num_positivos} valores positivos\n{media:.1f}')

main()    