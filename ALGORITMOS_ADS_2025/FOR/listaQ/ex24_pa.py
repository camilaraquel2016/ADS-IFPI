from utils import obter_real_maior_que_0, obter_inteiro_positivo

def exibir_pa(razao_pa, primeiro_termo, qtd_termos):
    final = qtd_termos + 1
    termo_a_ser_exibido = primeiro_termo

    for termo in range(1, final, 1):
        print(termo_a_ser_exibido)

        termo_a_ser_exibido += razao_pa


def main():
    razao_pa = obter_real_maior_que_0('Razão da PA: ')
    primeiro_termo = obter_real_maior_que_0('Primeiro termo: ')
    qtd_termos = obter_inteiro_positivo('Quantidade de termos: ')
    exibir_pa(razao_pa, primeiro_termo, qtd_termos)

main()    