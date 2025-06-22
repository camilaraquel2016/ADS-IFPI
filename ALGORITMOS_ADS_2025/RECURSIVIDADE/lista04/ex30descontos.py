from utils import obter_inteiro_maior_que_0, obterNumRealLimiteMin

def obter_percentual_de_desconto(qtd):
    if qtd <= 10:
        return 0
    elif qtd <= 20:
        return 0.1
    elif qtd <= 50:
        return 0.2
    else:
        return 0.25


def gerenciar_vendas():
    nome_do_produto = str(input('Insira o nome do produto: (flag = FIM) ')).upper()
   
    if nome_do_produto == 'FIM':
        return 'Compras encerradas...' 
    
    preco_unitario = obterNumRealLimiteMin('Insira o valor unitário do produto: R$', 1)
    qtd = obter_inteiro_maior_que_0('Quantidade: ')
    percentual_de_desconto = obter_percentual_de_desconto(qtd)
    valor_inicial = preco_unitario * qtd
    valor_do_desconto = percentual_de_desconto * valor_inicial
    valor_com_desconto = valor_inicial - valor_do_desconto
    print(f'Nome do produto: {nome_do_produto}\nValor total a pagar: R${valor_com_desconto:.2f}\n')
    
    return gerenciar_vendas()


def main():
    print(gerenciar_vendas())    

main()