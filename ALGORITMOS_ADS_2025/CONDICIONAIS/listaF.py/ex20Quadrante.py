from utils import entradaFloat, validarNumLimiteFloat

def localizarAngulo(angulo):
    if angulo == 0 or angulo == 360:
        return 'eixo do 4° e 1° quadrante'
    elif angulo == 90:
        return 'eixo do 1° e 2° quadrante'
    elif angulo == 180:
        return 'eixo do 2° e 3° quadrante'
    elif angulo == 270:
        return 'eixo do 3° e 4° quadrante'
    
    elif angulo < 90:
        return '1° quadrante'
    elif angulo < 180:
        return '2° quadrante'
    elif angulo < 270:
        return '3° quadrante'
    else:
        return '4° quadrante'
    

def main():
    angulo = entradaFloat('Digite o valor do ângulo: ')
    angulo = validarNumLimiteFloat(angulo, 0, 360, 'Digite o valor do ângulo: ')
    
    localizacao = localizarAngulo(angulo)

    print(f'O ângulo de {angulo}° está no {localizacao}')


main()