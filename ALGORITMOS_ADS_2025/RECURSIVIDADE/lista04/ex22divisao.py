from utils import obterNumInteiroPositivo

def obter_resultado(num1, num2, quociente = 0): 
    if num1 < num2:
        return quociente, num1
    
    num1 -= num2 
    quociente += 1 
    return obter_resultado(num1, num2, quociente)


def main():
    num1 = obterNumInteiroPositivo('Primeiro número: ')
    num2 = obterNumInteiroPositivo('Segundo número: ')
    resultado = obter_resultado(num1, num2)
    quociente = resultado[0]
    resto = resultado[1]
    print(f'{num1} / {num2} = {quociente} e sobra {resto}')

main()