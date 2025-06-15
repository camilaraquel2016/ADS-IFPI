from utils import entradaFloat


def calcularIMC(peso, altura):
    return peso / altura ** 2


def classificacaoIMC(peso, altura):
    imc = calcularIMC(peso, altura)

    if imc < 25:
        return 'Peso normal'
    elif imc <= 30:
        return 'Obeso'
    else:
        return 'Obesidade mórbida'
    

def main():
    peso = entradaFloat('Digite seu peso Kg: ')
    altura = entradaFloat('Digite sua altura em metros: ')

    imc = calcularIMC(peso, altura)
    classificacao = classificacaoIMC(peso, altura)

    print(f'Seu IMC é: {imc:.2f} e sua classificação é: "{classificacao}"')


main()