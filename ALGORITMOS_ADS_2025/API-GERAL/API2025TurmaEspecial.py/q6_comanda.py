#início 25/05 10:04
# fim 25/05 12:15

from time import sleep
from q1_number_utils import obterNumInteiroPositivo, obterNumInt

def cardapio():
    return f'''
-=-=-CARDÁPIO-=-=-    
Cerveja    - R$9,00
Tira-gosto - R$39,00
Água       - R$5,00

Código (C) - Cerveja
Código (T) - Tira-gosto
Codigo (A) - Água

'''


def menuOperacoes():
    return f'''
-=-MENU DE OPÇÕES-=-    
1 -  Inserir produtos
2 -  Imprimir a conta
'''

def obterValor(qtd: int, item: str):
    if item == 'C':
        valor = 9
    elif item == 'T':
        valor = 39
    elif item == 'A':
        valor = 5

    valorFinalItem = qtd * valor
    return valorFinalItem            


def obterTaxaDeServico(qtdCerveja, valorDaConta):
    return 0 if qtdCerveja > 10 or valorDaConta > 200 else 10


def pedirOperacao(label: str):
    while True:
        print(menuOperacoes())
        opcao = obterNumInt(label)
        if opcao == 1 or opcao == 2:
            return opcao
        else:
            print('Opção inválida')


def pedirItem():
    print(cardapio())
    return str(input('Insira a quantidade e o item desejado: '))



def calcularValorFinalDaconta(somaTotal, taxaDeServico):
    return taxaDeServico / 100 * somaTotal + somaTotal


def confirmacao():
    print()
    sleep(1)
    print('Item adicionado a conta com sucesso!')
    sleep(1)
    print()
    
    

def acumularItens():
    somaTotal = 0
    qtdCervejas = 0
    while True:
        itemCardapio = pedirItem()
        qtd = int(itemCardapio[0])
        item = itemCardapio[-1].upper()
        valorFinalDoItem = obterValor(qtd, item)
        somaTotal += valorFinalDoItem
        confirmacao()

        if item == 'C':
            qtdCervejas += qtd

        opcao = pedirOperacao('Opção: ')

        if opcao != 1:
            break
    return somaTotal, opcao, qtdCervejas   


def gerenciarConta():
    opcao = pedirOperacao('Opção: ')
    if opcao == 2:
        print('Ainda não há nenhum item cadastrado na comanda!')
    else:
        acumuloDosItens = acumularItens()
        somaTotal = float(acumuloDosItens[0])
        qtdCerveja = int(acumuloDosItens[2])
        taxaDeServico = obterTaxaDeServico(qtdCerveja, somaTotal)
        valorDoServico = taxaDeServico / 100 * somaTotal
        opcao = acumuloDosItens[1]
        if opcao == 2:
            qtdPessoas = obterNumInteiroPositivo('Quantidade de pessoas para pagar a conta: ')
            valorFinal = calcularValorFinalDaconta(somaTotal, taxaDeServico)
            valorPorPessoa = valorFinal / qtdPessoas
            print(apresentarResumoFinal(qtdPessoas, valorFinal, somaTotal, valorDoServico, valorPorPessoa))


def apresentarResumoFinal(qtdPessoas, valorFinal, valorSemTaxa, valorDoServico, valorPorPessoa):
    return f'''
Valor da conta: {valorSemTaxa:.2f}
Valor da taxa de serviço: R${valorDoServico:.2f}
Valor da conta final: R${valorFinal:.2f}
Quantidade de pessoas: {qtdPessoas}
Valor por pessoa: R${valorPorPessoa:.2f}
'''


def main():
    print('-=-RESTAURANTE BOM PALADAR-=-')
    gerenciarConta()


main()




        



        

     

    
   

