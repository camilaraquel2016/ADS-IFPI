from utils import converter_maisculo, obter_real_positivo


def imprimir_saida(menor_peso, maior_peso, maior_altura, menor_altura, nome_alta, nome_baixa, nome_magra, nome_gorda):
    return f'''
    Mais magra: {nome_magra} - {menor_peso} Kg
    Mais gorda: {nome_gorda} - {maior_peso} Kg
    Mais alta: {nome_alta} - {maior_altura} cm
    Mais baixa: {nome_baixa} - {menor_altura} cm
'''


def obter_resultado():
    nome_mais_alta = ''
    nome_mais_baixa = ''
    nome_mais_gorda = ''
    nome_mais_magra = ''

    maior_altura = 0
    menor_altura = float('inf')

    maior_peso = 0
    menor_peso = float('inf')

    nome = converter_maisculo(input('Nome: (flag = FIM) '))
    
    while nome != 'FIM':
        peso = obter_real_positivo('Peso: (kg) ')
        altura = obter_real_positivo('Altura: (metros) ')

        if altura > maior_altura:
            maior_altura = altura
            nome_mais_alta = nome

        if altura < menor_altura:
            menor_altura = altura
            nome_mais_baixa = nome     

        if peso > maior_peso:
            maior_peso = peso
            nome_mais_gorda = nome

        if peso < menor_peso:
            menor_peso = peso
            nome_mais_magra = nome

        nome = converter_maisculo(input('Nome: (flag = FIM) '))       

    return imprimir_saida(menor_peso, maior_peso, maior_altura, menor_altura, nome_mais_alta, nome_mais_baixa, nome_mais_magra, nome_mais_gorda)
     

def main():
    resultado = obter_resultado()
    print(resultado)

main()
