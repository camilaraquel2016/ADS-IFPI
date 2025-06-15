from utils import entradaFloat

def calcularDelta(a, b, c):
    return b ** 2 - 4 * a * c


def calcularRaiz1(a, b, c):
    delta = calcularDelta(a, b, c)
    
    return (- b + (delta ** (0.5))) / 2 * a


def calcularRaiz2(a, b, c):
    delta = calcularDelta(a, b, c)
    
    return (- b - (delta ** (0.5))) / 2 * a


def calcularRaizUnica(a, b, c):
    return (- b) / 2 * a


def calcularEquacao(a, b, c):
    delta = calcularDelta(a, b, c)
    raiz1 = calcularRaiz1(a, b, c)
    raiz2 = calcularRaiz2(a, b, c)
    raizunica = calcularRaizUnica(a, b, c)
    
    if delta > 0:
        return f'Raíz 1: {raiz1:.2f}\nRaíz 2: {raiz2:.2f}'
    elif delta < 0:
        return f'Essa equação não possui raizes reais'
    else:
        return f'Raíz única: {raizunica:.2f}'


def validarCoeficienteA(coeficienteA):
    if coeficienteA != 0:
        return coeficienteA
    else:
        print('Coeficiente A deve ser diferente de 0!')
        coeficienteA = entradaFloat('Coeficiente A: ')
        return validarCoeficienteA(coeficienteA)
    
    
def main():
    coefA = entradaFloat('Coeficiente A: ')

    coefA = validarCoeficienteA(coefA)
    coefB = entradaFloat('Coeficiente B: ')
    coefC = entradaFloat('Coeficiente C: ')

    print(calcularEquacao(coefA, coefB, coefC))

main()    



