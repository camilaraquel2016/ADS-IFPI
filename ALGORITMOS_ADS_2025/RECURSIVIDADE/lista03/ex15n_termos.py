from utils import obter_inteiro_maior_que_0

def exibir_n_termos(qtd_termos, num = 1, aumento = 1):
    print(num)
    
    if qtd_termos > 1:
        qtd_termos -= 1
        aumento += 1
        num += aumento
        return exibir_n_termos(qtd_termos, num, aumento)
    

def main():
    qtd_termos = obter_inteiro_maior_que_0('Insira a quantidade de termos: ')
    exibir_n_termos(qtd_termos)

main()    