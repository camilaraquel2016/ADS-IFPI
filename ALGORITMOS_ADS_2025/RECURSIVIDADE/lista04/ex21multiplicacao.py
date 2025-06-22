from utils import obterNumInteiroPositivo

def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def obter_menor(num1, num2):
    return num1 if num1 < num2 else num2


def obter_produto(maior, menor, contador = 0, num = 0):

    if contador < menor:  
        num += maior 
        contador += 1
        return obter_produto(maior, menor, contador, num)
    
    return num
    

def main():
    num1 = obterNumInteiroPositivo('Primeiro número: ')
    num2 = obterNumInteiroPositivo('Segundo número: ')
    maior = obter_maior(num1, num2)
    menor = obter_menor(num1, num2)
    produto = obter_produto(maior, menor, 0, 0)
    print(f'{num1} X {num2} = {produto}')

main()


