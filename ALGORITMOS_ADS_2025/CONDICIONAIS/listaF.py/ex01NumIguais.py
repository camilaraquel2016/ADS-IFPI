from utils import entradaFloat

def QuantNumIguais(num1, num2, num3):
    if num1 == num2 == num3:
        return 'todos os números iguais'
    elif num1 != num2 and num2 != num3 and num1 != num3:
        return 'todos os números diferentes'
    else:
        return '2 números iguais'
    

def main():
    num1 = entradaFloat('Digite o primeiro número: ')    
    num2 = entradaFloat('Digite o segundo número: ')
    num3 = entradaFloat('Digite o terceiro número: ')
    
    print(f'A sequência: {num1}, {num2}, {num3} apresenta {QuantNumIguais(num1, num2, num3)}')
    
main()