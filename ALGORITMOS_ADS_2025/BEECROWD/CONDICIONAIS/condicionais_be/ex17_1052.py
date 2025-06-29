def obter_mes(num_do_mes: int, meses_do_ano: list):
    return meses_do_ano[num_do_mes - 1]


def main():
    num_do_mes = int(input())
    meses_do_ano = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    mes_escolhido = obter_mes(num_do_mes, meses_do_ano)
    print(mes_escolhido)

main()        