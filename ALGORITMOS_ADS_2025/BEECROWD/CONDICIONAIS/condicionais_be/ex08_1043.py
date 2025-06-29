def forma_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1


def calcular_perimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


def calcular_area_trapezio(lado1, lado2, lado3):
    return (lado1 + lado2) * lado3 / 2


def main():
    lados = input().split()

    lado1 = float(lados[0])
    lado2 = float(lados[1])
    lado3 = float(lados[2])

    if forma_triangulo(lado1, lado2, lado3):
        perimetro = calcular_perimetro(lado1, lado2, lado3)
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area = calcular_area_trapezio(lado1, lado2, lado3)
        print(f'Area = {area:.1f}')

main()            