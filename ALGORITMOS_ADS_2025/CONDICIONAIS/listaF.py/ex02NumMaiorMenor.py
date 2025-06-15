from utils import entradaFloat

def MaiorMenorNum(num1, num2):
    if num1 > num2:
        return f'{num1} é maior que {num2}'
    elif num2 > num1:
        return f'{num2} é maior que {num1}'
    else:
        return 'Os números são iguais'
    
def main():  
    num1 = entradaFloat('Digite o primeiro número: ')
    num2 = entradaFloat('Digite o segundo número: ')

    print(MaiorMenorNum(num1, num2))

main()
    

