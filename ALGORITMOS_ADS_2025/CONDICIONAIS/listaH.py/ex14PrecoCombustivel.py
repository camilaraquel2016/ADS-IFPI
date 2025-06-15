from time import sleep

def menu():
    return f'A - Álcool\nG - Gasolina'


def valorFinalAlcool(qtdLitros, precoAlcool):
    if qtdLitros <= 20:
        valorLitro = 0.97 * precoAlcool 
    else:
        valorLitro = 0.95 * precoAlcool
    return qtdLitros * valorLitro


def valorFinalGasolina(qtdLitros, precoGasolina):
    if qtdLitros <= 20:
        valorLitro = 0.96 * precoGasolina
    else:
        valorLitro =  0.94 * precoGasolina
    return qtdLitros * valorLitro

def obterResposta():
    print(menu())
    print('Qual combustível usará para abastecer? ')
    resposta = str(input('Insira A ou G: ')).upper()

    while resposta != 'A' and resposta != 'G':
        sleep(1)
        print(' ')
        print('Resposta invalida!')
        sleep(1)
        print(' ')
        print(menu())
        print('Qual combustível usará para abastecer? ')
        resposta = str(input('Insira A ou G: ')).upper()
    return resposta

    


def main():
    precoGasolina = 2.5
    precoAlcool = 1.9

    tipoCombustivel = obterResposta()
    if tipoCombustivel == 'A':
        tipoCombustivel = 'Álcool'
    else:
        tipoCombustivel = 'Gasolina'     
    
    quantLitros = float(input('Quantos litros irá abastecer? '))

    if tipoCombustivel == 'Álcool':
        valorTotal = valorFinalAlcool(quantLitros, precoAlcool)
    else:
        valorTotal = valorFinalGasolina(quantLitros, precoGasolina)

    print(f'{quantLitros} litros de {tipoCombustivel} custará R${valorTotal:.2f} no total')        


main()    