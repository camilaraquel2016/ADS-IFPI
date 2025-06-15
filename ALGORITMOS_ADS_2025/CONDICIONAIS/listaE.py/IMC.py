from utils import entradaFloat

def calcularIMC(peso, altura):
    return peso / altura ** 2


def classificarIMC(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'Sobrepeso'
    elif imc <= 34.9:
        return 'Obesidade grau 1'
    elif imc <= 39.9:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'
    

def main():
    print('-=-=-=-SISTEMA DE VERIFICAÇÃO DO PESO IDEAL-=-=-=-')
    peso = entradaFloat('Insira seu peso em Kg: ')
    altura = entradaFloat('Insira sua altura em metros: ')
    imc = calcularIMC(peso, altura)
    classificacaoIMC = classificarIMC(imc)
    print(f'Seu imc é {imc:.2f} e você está na seguinte situação: "{classificacaoIMC}" ')


main()