from utils import obterNumInteiroPositivo, obterNumRealPositivo

def saida(maior_peso, menor_peso, num_do_mais_pesado, num_do_menos_pesado):

    if maior_peso == 0:
        return f'NENHUM BOI CADASTRADO'
    
    return f'''
    -=-MAIS PESADO-=-
    N° de identificação: {num_do_mais_pesado}
    Peso: {maior_peso} Kg

    -=-MENOS PESADO-=-
    N° de identificação: {num_do_menos_pesado}
    Peso: {menor_peso} Kg'''


def obter_dados(maior_peso = 0, menor_peso = float('inf'), num_do_mais_pesado = '', num_do_menos_pesado = ''):
    num_identificacao = obterNumInteiroPositivo('N° de identificação: (flag = 0) ')

    if num_identificacao == 0:
        return saida(maior_peso, menor_peso, num_do_mais_pesado, num_do_menos_pesado)
    
    peso = obterNumRealPositivo('Peso: (Kg) ')

    if peso > maior_peso:
        maior_peso = peso
        num_do_mais_pesado = num_identificacao

    if peso < menor_peso:
        menor_peso = peso
        num_do_menos_pesado = num_identificacao

    return obter_dados(maior_peso, menor_peso, num_do_mais_pesado, num_do_menos_pesado)
    

def main():
    print(obter_dados(0, float('inf'), '', '')) 

main()       

    

