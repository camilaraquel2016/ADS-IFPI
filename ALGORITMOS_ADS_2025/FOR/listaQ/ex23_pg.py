from utils import obter_real_maior_que_0, obter_inteiro_maior_que_0

def exibir_n_termos(razao_pg, primeiro_termo, qtd_termos):
    final = qtd_termos + 1

    termo_a_ser_exibido = primeiro_termo

    for termo in range(1, final, 1):
        print(f'{termo_a_ser_exibido:.2f}')
        termo_a_ser_exibido *= razao_pg


def main():
    razao_pg = obter_real_maior_que_0('Razão da PG: ')
    primeiro_termo = obter_real_maior_que_0('Primeiro termo: ')
    qtd_termos = obter_inteiro_maior_que_0('Quantidade de termos: ')

    exibir_n_termos(razao_pg, primeiro_termo, qtd_termos)

main()    