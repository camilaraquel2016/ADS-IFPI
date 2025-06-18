from itertools import count
from utils import obter_real_positivo, obter_inteiro_maior_que_0, converter_maisculo

def obter_percentual_desconto(qtd_do_produtos):
    if qtd_do_produtos <= 10:
        return 0
    elif qtd_do_produtos <= 20:
        return 0.1
    elif qtd_do_produtos <= 50:
        return 0.2
    else:
        return 0.25


def gerenciar_vendas():

    for produto in count():
        nome_do_produto = converter_maisculo(str(input('Nome do produto: (flag = FIM) ')))

        if nome_do_produto == 'FIM':
            break

        valor_do_produto = obter_real_positivo('Valor unitário do produto: R$')
        qtd_comprada = obter_inteiro_maior_que_0('Quantidade comprada desse produto: ')

        percentual_de_desconto = obter_percentual_desconto(qtd_comprada)

        valor_final = (valor_do_produto * qtd_comprada) * (1 - percentual_de_desconto)

        print(f'Nome do produto: {nome_do_produto}\nValor total: R${valor_final:.2f}')
        print( )

gerenciar_vendas()
