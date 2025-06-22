from utils import obterNumReal, obter_inteiro_maior_que_0


def exibir_pa(razao_pa, termo_a_ser_exibido, qtd_termos, contador = 0):
    if contador < qtd_termos:
        print(termo_a_ser_exibido)
        termo_a_ser_exibido += razao_pa
        contador += 1
        return exibir_pa(razao_pa, termo_a_ser_exibido, qtd_termos, contador)
    
    return 'FIM'


def main():
    razao_pa = obterNumReal('Razão da PA: ')
    primeiro_termo = obterNumReal('Primeiro termo: ')
    qtd_termos = obter_inteiro_maior_que_0('N termos: ')
    print(f'-=-Os {qtd_termos} primeiros termos da PA de razão {razao_pa} e A1 = {primeiro_termo}-=-')
    print(exibir_pa(razao_pa, primeiro_termo, qtd_termos, 0))

main()    
