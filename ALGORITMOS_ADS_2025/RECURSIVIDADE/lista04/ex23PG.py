from utils import obterNumRealLimiteMin, obterNumReal, obter_inteiro_maior_que_0

def exibir_pg(razao_pg, termo_a_ser_exibido, qtd_termos, contador = 0):
    
    if contador < qtd_termos:
        print(termo_a_ser_exibido)
        termo_a_ser_exibido *= razao_pg
        contador += 1
        return exibir_pg(razao_pg, termo_a_ser_exibido, qtd_termos, contador)
    
    return 'FIM'
    

def main():
    razao_pg = obterNumRealLimiteMin('Razão da PG: ', 0.1)
    primeiro_termo = obterNumReal('Primeiro termo: ')
    qtd_termos = obter_inteiro_maior_que_0('N termos: ')
    print(f'Os {qtd_termos} primeiros termos da PG de razão {razao_pg} e A1 = {primeiro_termo}')
    print(exibir_pg(razao_pg, primeiro_termo, qtd_termos, 0))

main()

