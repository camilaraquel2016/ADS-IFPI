from utils import obterNumInt
from time import sleep

# funcao para validar entrada do menu 1, 2 ou 3 

def menu():
    return '''
    -=-=-=-MENU-=-=-=-
    1 - Adicionar item
    2 - Imprimir lista
    3 - Sair
    -=-=-=-=-=-=-=-=-=-
    '''



def obterOpcao():
    print(menu())
    opcao = obterNumInt('Sua opção: (1 a 3) ')
    print(' ')

    while opcao != 1 and opcao != 2 and opcao != 3:
        sleep(1)
        print('Opção inválida!')
        sleep(1)
        print(menu())
        sleep(1)
        opcao = obterNumInt('Sua opção: (1 a 3) ')
        
    return opcao


def adicionarItem():
    nomeProd = str(input('Nome do produto: ')).capitalize()
    especificacao = str(input('Especificação do produto: Ex: 5kg, 1L, 900g... '))
    
    return f'{nomeProd} ({especificacao})'


def obterPagemento(valor):
    if valor <= 30:
        print('OPÇÃO 1    - ESPÉCIE\nOPÇÃO 2.1  - PARCELAR EM ATÉ 6X com juros')
        formaDePagamento = validarPagemento(valor)
    elif valor <= 100:
        print('OPÇÃO 1    - ESPÉCIE\nOPÇÃO 2.1  - PARCELAR EM ATÉ 6X com juros\nOPÇÃO 2.2  - PARCELAR EM ATÉ 3X sem juros ')
        formaDePagamento = validarPagemento(valor)
    else:
        print('OPÇÃO 1    - ESPÉCIE\nOPÇÃO 2.1  - PARCELAR EM ATÉ 6X com juros\nOPÇÃO 2.3  - PARCELAR EM ATÉ 5X sem juros ')  
        formaDePagamento = validarPagemento(valor)
    return formaDePagamento    
        
def validarPagemento(valor):
    opcaoDePagamento = float(input('Forma de pagamento: '))

    if valor <= 30:
        if opcaoDePagamento != 1 and opcaoDePagamento != 2.1:
            print('OPÇÃO DE PAGAMENTO INVÁLIDA!')
            return validarPagemento(valor)
        return opcaoDePagamento
    
    elif valor <= 100:
        if opcaoDePagamento != 1 and opcaoDePagamento != 2.1 and opcaoDePagamento != 2.2:
            print('OPÇÃO DE PAGAMENTO INVÁLIDA!')
            return validarPagemento(valor)
        return opcaoDePagamento
    
    else:
        if opcaoDePagamento != 1 and opcaoDePagamento != 2.1 and opcaoDePagamento != 2.3:
            print('OPÇÃO DE PAGAMENTO INVÁLIDA!')
            return validarPagemento(valor)
        return opcaoDePagamento

    
def espaco(msgAtual, limiteCaractere):
    msgAtual = str(msgAtual)

    tamanhoDaMsgAtual = len(msgAtual)
    return limiteCaractere - tamanhoDaMsgAtual

def exibirListaFinal(somaTotal, listaDeItens):
    espaco1 = 16 * ' '
    espaco2 = espaco(somaTotal, 11) * ' '
    listaFinal = f'{'-=' * 6}PESQUISA DE PREÇOS{'-=' * 6}\n{listaDeItens}{'-=' * 21}\nValor total:{espaco1}R${espaco2}{somaTotal:.2f}'
    return listaFinal
    

def formatarItem(contador, novoItem, valorProd):
    item = f'{contador} - {novoItem}R$'
    espacoNecessario = espaco(item, 30) * ' '
    espacoNecessario2 = espaco(valorProd, 10) * ' '
    item = f'{contador} - {novoItem}{espacoNecessario}R${espacoNecessario2}{valorProd:.2f}\n'
    return item


def gerenciarMenu():
    opcao = obterOpcao()
    if opcao == 2:
        return f'Não há produto cadastrados!'
    if opcao == 3:
        return f'Programa encerrado...'
    
    listaDeintens = ''
    somaTotal = 0
    contador = 0
    
    while opcao == 1:
        contador += 1
        novoItem = adicionarItem()
        valorProd = float(input('Valor do produto: '))
        item = formatarItem(contador, novoItem, valorProd)
        listaDeintens += item
        somaTotal += valorProd
        opcao = obterOpcao()
        if opcao == 2:
            if contador >= 1:
              return exibirListaFinal(somaTotal, listaDeintens)
        if opcao == 3:
            return 'Programa encerrado...'    





def exibirPagamentoFinal(pagamento, valor, taxaDeJuros):
    if pagamento == 1:
        print(f'O cliente ira pagar o valor R${valor:.2f} em espécie')
    elif pagamento == 2.2:
        quantParcelas = obterQuantParcelas(1, 3)
        valorDaParcela = valor / quantParcelas
        print(f'O cliente irá pagar {quantParcelas} parcelas de R${valorDaParcela:.2f} cada uma')
    elif pagamento == 2.3:
        quantParcelas = obterQuantParcelas(1, 5)
        valorDaParcela = valor / quantParcelas
        print(f'O cliente irá pagar {quantParcelas} parcelas de R${valorDaParcela:.2f} cada uma')   
    else:
        quantParcelas = obterQuantParcelas(1, 6)
        print(f'O cliente irá fazer o pagamento com juros compostos de {taxaDeJuros * 100}%')
        exibirJurosCompostos(quantParcelas, valor, taxaDeJuros)


def exibirJurosCompostos(qtdParcelas, valor, taxaDeJuros):
    valorDaParcelaInicial = valor / qtdParcelas
    contador = 1
    valorDaParcela = valorDaParcelaInicial

    while contador <= qtdParcelas:
        print(f'{contador}° parcela - R${valorDaParcela:.2f}')
        valorDaParcela = valorDaParcela + (taxaDeJuros * valorDaParcela)
        contador +=1 

def obterQuantParcelas(min, max):
    qtdParcelas = float(input('Quantidade de parcelas: '))

    while qtdParcelas < min or qtdParcelas > max:
        print('Número de parcelas inválido!')
        qtdParcelas = float(input('Quantidade de parcelas: '))
    return qtdParcelas

   


def main():
    taxaDeJuros = 5 / 100
    respostaFinal = gerenciarMenu()
    print(respostaFinal)

    valor = float(respostaFinal[-10:-1])

    if respostaFinal != 'Não Há produtos cadastrados' and respostaFinal != 'Programa encerrado': #signifca que o cliente deseja ver a lista de 
        print(' ')
        print('-=-MENU DE PAGAMENTOS-=-')
        pagamento = obterPagemento(valor)
        exibirPagamentoFinal(pagamento, valor, taxaDeJuros)
    else:
        print(gerenciarMenu())

         
main()