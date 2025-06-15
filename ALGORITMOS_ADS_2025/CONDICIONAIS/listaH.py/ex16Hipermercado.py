from time import sleep

def calcularKgFile(qtdKg):
    return 4.9 if qtdKg <= 5 else 5.8


def calcularKgAlcatra(qtdKg):
    return 5.9 if qtdKg <= 5 else 6.8


def calcularKgPicanha(qtdKg):
    return 6.9 if qtdKg <= 5 else 7.8


def calcularValor(qtdKg, tipoCarne):
    if tipoCarne == 'Filé':
        valorKg = calcularKgFile(qtdKg)
        valorTotal = valorKg * qtdKg
    elif tipoCarne == 'Alcatra':
        valorKg = calcularKgAlcatra(qtdKg)
        valorTotal = valorKg * qtdKg
    elif tipoCarne == 'Picanha':
        valorKg = calcularKgPicanha(qtdKg)
        valorTotal = valorKg * qtdKg
    return valorTotal


def menu():
    return f'1 - Filé\n2 - Alcatra\n3 - Picanha'


def calcularPercentualDesconto(formaDePagamento):
    return 0.05 if formaDePagamento == 'Cartão Tabajara' else 0


def pedirTipoDeCarne():
    print(menu())
    tipoCarne = int(input('Sua escolha: '))

    if tipoCarne != 1 and tipoCarne != 2 and tipoCarne != 3:
        print(' ')
        sleep(1)
        print('Tipo de carne inválido!')
        sleep(1)
        print(' ')
        return pedirTipoDeCarne()
    else:
        if tipoCarne == 1:
            return 'Filé'
        if tipoCarne == 2:
            return 'Alcatra'
        if tipoCarne == 3:
            return 'Picanha'

def menuPagamento():
    return f'1 - Espécie\n2 - Pix\n3 - Cartão Tabajara'



def pedirFormaDePagamento():
    print(menuPagamento())
    formaDePagamento = int(input('Forma de pagamento: '))

    if formaDePagamento != 1 and formaDePagamento != 2 and formaDePagamento != 3:
        sleep(1)
        print(' ')
        print('Forma de pagamento inválida!')
        return pedirFormaDePagamento()
    else:
        if formaDePagamento == 1:
            return 'Espécie'
        if formaDePagamento == 2:
            return 'Pix'
        if formaDePagamento == 3:
            return 'Cartão Tabajara'
        




def main():
    tipo = pedirTipoDeCarne()
    
    qtdCarne = float(input(f'Qunatos Kg de {tipo} irá comprar? '))

    formaDePagamento = pedirFormaDePagamento()

    

    valorTotal = calcularValor(qtdCarne, tipo)

    desconto = valorTotal * calcularPercentualDesconto(formaDePagamento)
    
    valorFinal = valorTotal - desconto

    print('-=' * 10)

    print(f'Tipo de carne: {tipo}\nQuantidade de carne: {qtdCarne} Kg\nPreço total: R${valorTotal:.2f}\nTipo de pagamento: {formaDePagamento}\nValor Desconto: R${desconto:.2f}\nValor a pagar: R${valorFinal:.2f}')
    
    




main()

            

