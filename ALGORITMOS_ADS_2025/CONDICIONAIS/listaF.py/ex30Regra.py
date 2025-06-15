from utils import entradaInt, valorMilhar, valorCentena, valorDezena, valorUnidade, validarNum4Dig

def obedeceRegra(num):
    milhar = valorMilhar(num)
    centena = valorCentena(num)
    dezena = valorDezena(num)
    unidade = valorUnidade(num)

    valor1 = milhar * 10 + centena
    valor2 = dezena * 10 + unidade

    somaNum = valor1 + valor2
    quadradoSomaNum = somaNum ** 2

    return quadradoSomaNum == num



def main():
    num = entradaInt('Insira um número de 4 dígitos: ')
    num = validarNum4Dig(num)
 
    if obedeceRegra(num):
        print(f'O número {num} obedece a regra')
    else:
        print(f'O número: {num} NÃO obedece a regra')     

main()