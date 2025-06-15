from utils import entradaFloat, validarLimiteMinFloat

def eh_triangulo(ang1, ang2, ang3):
    return ang1 + ang2 + ang3 == 180


def eh_triangulo_acutangulo(ang1, ang2, ang3):
    return ang1 < 90 and ang2 < 90 and ang3 < 90 


def eh_triangulo_retangulo(ang1, ang2, ang3):
    return ang1 == 90 or ang2 == 90 or ang3 == 90


def eh_triangulo_obtusangulo(ang1, ang2, ang3):
    return ang1 > 90 or ang2 > 90 or ang3 > 90


def classificarTriangulo(ang1, ang2, ang3):
    if eh_triangulo(ang1, ang2, ang3):
        
        if eh_triangulo_acutangulo(ang1, ang2, ang3):
            tipo = 'Acutângulo'
        elif eh_triangulo_retangulo(ang1, ang2, ang3):
            tipo = 'Retângulo'
        else:
            tipo = 'Obtusângulo'

        return f'É um triângulo do tipo "{tipo}"'    

    else:
        return 'Esses ângulos NÃO formam um triângulo'


def main():
    print('-=-=-Analisador de triângulo-=-=-')    

    ang1 = entradaFloat('Digite o valor do primeiro ângulo: ') 
    ang1 = validarLimiteMinFloat(ang1, 1, 'Digite o valor do primeiro ângulo: ')

    ang2 = entradaFloat('Digite o valor do segundo ângulo: ') 
    ang2 = validarLimiteMinFloat(ang2, 1, 'Digite o valor do segundo ângulo: ') 

    ang3 = entradaFloat('Digite o valor do terceiro ângulo: ') 
    ang3 = validarLimiteMinFloat(ang3, 1, 'Digite o valor do terceiro ângulo: ')         

    print(classificarTriangulo(ang1, ang2, ang3))
   

main()    




