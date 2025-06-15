from itertools import count
from utils import obter_real_positivo, obter_inteiro_positivo

def imprimir_saida(num_mais_pesado, num_menos_pesado, maior_peso, menor_peso):
    return f'''
    Mais pesado: N°{num_mais_pesado} - {maior_peso} Kg
    Menos pesado: N°{num_menos_pesado} - {menor_peso} Kg
'''


def obter_resultados():
    maior_peso = 0
    menor_peso = float('inf')

    num_mais_pesado = ''
    num_menos_pesado = ''

    for boi in count():
        num_identificacao = obter_inteiro_positivo(f'Número de identificação do {boi + 1}° boi: (flag = 0) ')
        
        if num_identificacao == 0:
            return imprimir_saida(num_mais_pesado, num_menos_pesado, maior_peso, menor_peso)


        peso_do_boi = obter_real_positivo(f'Peso do {boi + 1}° boi: (Kg) ')

        if peso_do_boi > maior_peso:
            maior_peso = peso_do_boi
            num_mais_pesado = num_identificacao

        if peso_do_boi < menor_peso:
            menor_peso = peso_do_boi
            num_menos_pesado = num_identificacao


def main():
    resultado = obter_resultados()
    print(resultado)

main()    