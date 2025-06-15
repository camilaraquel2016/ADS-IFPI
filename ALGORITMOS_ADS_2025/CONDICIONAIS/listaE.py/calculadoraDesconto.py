from utils import entradaFloat, validarLimiteMinFloat, validarStr2Opcoes

def calcularPercentualDescontoBase(valor):
    if valor > 500:
        return 0.15
    elif valor >= 200:
        return 0.10
    elif valor >= 100:
        return 0.05
    else:
        return 0


def calcularPercentualDescontoVIP():
    return 0.05


def calcularPercentualDescontoAniversariante():
    return 0.03


def calcularDesconto(valor, percentualDesconto):
    return (percentualDesconto * valor)

  
def calcularValorFinal(valor, percentualDesconto):
    desconto = calcularDesconto(valor, percentualDesconto)
    return valor - desconto


def eh_vip(resposta):
    return resposta == 'S'


def eh_aniversariante(resposta):
    return resposta == 'S'


def main():
    valorCompras =  entradaFloat('Qual o valor das compras? R$')
    valorCompras = validarLimiteMinFloat(valorCompras, 1, 'Qual o valor das compras? R$')

    respostaVip = input('Você é um cliente VIP? Digite (S ou N): ').upper()
    respostaVip = validarStr2Opcoes(respostaVip, 'S', 'N', 'Você é um cliente VIP? Digite (S ou N): ')

    respostaAniversariante = input('Você está aniversariando hoje? Digite (S ou N): ').upper()
    respostaAniversariante = validarStr2Opcoes(respostaAniversariante, 'S', 'N', 'Você está aniversariando hoje? Digite (S ou N): ')

    percentualDescontoBase = calcularPercentualDescontoBase(valorCompras) 
    percentualDescontoVip = calcularPercentualDescontoVIP()
    percentualDescontoAniversariante = calcularPercentualDescontoAniversariante()
    
    percentualDescontoGeral = percentualDescontoBase

    if eh_vip(respostaVip):
        percentualDescontoGeral += percentualDescontoVip
    if eh_aniversariante(respostaAniversariante):
        percentualDescontoGeral += percentualDescontoAniversariante
   
    desconto = calcularDesconto(valorCompras, percentualDescontoGeral)
    valorFinal = calcularValorFinal(valorCompras, percentualDescontoGeral)    

    print(f'Valor inicial das compras: R${valorCompras:.2f}\nVocê recebeu um desconto de {percentualDescontoGeral * 100:.1f}%, ou seja, R${desconto:.2f} de desconto\nValor final das compras após desconto: R${valorFinal:.2f}')


main()


    
     