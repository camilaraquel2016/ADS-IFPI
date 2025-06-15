from utils import entradaInt, valorMilhar, valorCentena, valorDezena, valorUnidade, validarNum4Dig

def eh_quadrado_perfeito(num):
    milhar = valorMilhar(num)
    centena = valorCentena(num)
    dezena = valorDezena(num)
    unidade = valorUnidade(num)

    valor1 = milhar * 10 + centena
    valor2 = dezena * 10 + unidade

    soma = valor1 + valor2
    raizQuadradaNum = num ** (0.5)

    return raizQuadradaNum == soma



def main():
    num = entradaInt('Insira um número de 4 dígitos: ')
    num = validarNum4Dig(num)
 
    if eh_quadrado_perfeito(num):
        print(f'O número {num} é um quadrado perfeito')
    else:
        print(f'O número: {num} NÃO é um quadrado perfeito')     

main()