from utils import entradaFloat

def calcularAreaRetangulo(x1, x2, y1, y2):
    largura = abs(x2 - x1)
    altura = abs(y2 - y1)
    return largura * altura


def main():
    print('EIXO X')
    x1 = entradaFloat('x1: ')
    x2 = entradaFloat('x2: ')

    print('EIXO Y')
    y1 = entradaFloat('y1: ')
    y2 = entradaFloat('y2: ')

    area = calcularAreaRetangulo(x1, x2, y1, y2)

    print(f'Área do retângulo: {area:.2f}')


main()    
