from math import sqrt, degrees, acos

from utils import entradaFloat

def eh_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1


def calcularPerimetroTriangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


def calcularAreaHeron(lado1, lado2, lado3):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    areaTriangulo = sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
    return areaTriangulo


def anguloA(lado1, lado2, lado3):
    cossenoA = (lado2 ** 2 + lado3 ** 2 - lado1 ** 2) / (2 * lado2 * lado3)
    return degrees(acos(cossenoA))


def anguloB(lado1, lado2, lado3):
    cossenoB = (lado1 ** 2 + lado3 ** 2 - lado2 ** 2) / (2 * lado1 * lado3)
    return degrees(acos(cossenoB))


def anguloC(lado1, lado2, lado3):
    cossenoC = (lado1 ** 2 + lado2 ** 2 - lado3 ** 2) / (2 * lado1 * lado2)
    return degrees(acos(cossenoC))


def classificarPelosLados(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'Equilátero'
    elif lado1 != lado2 != lado3:
        return 'Escaleno'
    else:
        return 'Isósceles'


def classificarPelosAngulos(lado1, lado2, lado3):
    angulo1 = anguloA(lado1, lado2, lado3)
    angulo2 = anguloB(lado1, lado2, lado3)
    angulo3 = anguloC(lado1, lado2, lado3) 

    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return 'Acutângulo'
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return 'Retângulo'
    else:
        return 'Obtusângulo'
    

def main():
    print('-=-=Analisador de Triângulo=-=-')

    lado1 = entradaFloat('Lado 1: ')  
    lado2 = entradaFloat('Lado 2: ')
    lado3 = entradaFloat('Lado 3: ')

    if eh_triangulo(lado1, lado2, lado3):
        tipoTrianguloLados = classificarPelosLados(lado1, lado2, lado3)
        tipoTrianguloAngulos = classificarPelosAngulos(lado1, lado2, lado3)
        areaDoTriangulo = calcularAreaHeron(lado1, lado2, lado3)
        perimetroTriangulo = calcularPerimetroTriangulo(lado1, lado2, lado3)
        print(f'É um triângulo do tipo: "{tipoTrianguloLados}" e "{tipoTrianguloAngulos}"\nÁrea do triângulo: {areaDoTriangulo:.2f}\nPerímetro do triângulo: {perimetroTriangulo:.2f}')
    else:
        print('Essas medidas não podem formar um triângulo')
    
main()
