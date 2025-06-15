from utils import entradaFloat, validarLimiteMinFloat

def eh_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 >= lado3 and lado1 + lado3 >= lado2 and lado2 + lado3 >= lado1


def eh_triangulo_equilatero(lado1, lado2, lado3):
    return lado1 == lado2 == lado3


def eh_triangulo_isosceles(lado1, lado2, lado3):
    return (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1)


def eh_triangulo_escaleno(lado1, lado2, lado3):
    return lado1 != lado2 and lado1 != lado3 and lado2 != lado3


def classificarTriangulo(lado1, lado2, lado3):
    if eh_triangulo(lado1, lado2, lado3):

        if eh_triangulo_equilatero(lado1, lado2, lado3):
            tipo = 'Equilátero'
        elif eh_triangulo_isosceles(lado1, lado2, lado3):
            tipo = 'Isósceles'
        elif eh_triangulo_escaleno(lado1, lado2, lado3):
            tipo = 'Escaleno'

        return f'É um triângulo do tipo "{tipo}"'
    else:
        return 'Essas medidas NÃO formam um triângulo'


def main():
    print('-=-=-Analisador de triângulo-=-=-')

    lado1 = entradaFloat('Digite o primeiro lado do triângulo: ')   
    lado1 = validarLimiteMinFloat(lado1, 1, 'Digite o primeiro lado do triângulo: ')

    lado2 = entradaFloat('Digite o segundo lado do triângulo: ')
    lado2 = validarLimiteMinFloat(lado2, 1, 'Digite o segundo lado do triângulo: ')
    
    lado3 = entradaFloat('Digite o terceiro lado do triângulo: ')
    lado3 = validarLimiteMinFloat(lado3, 1, 'Digite o terceiro lado do triângulo: ')
    
    print(classificarTriangulo(lado1, lado2, lado3))


main()    