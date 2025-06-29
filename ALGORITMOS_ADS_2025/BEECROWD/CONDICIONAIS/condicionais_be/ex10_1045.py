def forma_triangulo(a, b, c):
    return a < b + c


def obter_tipo1(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        return 'TRIANGULO RETANGULO'
    elif a ** 2 > b ** 2 + c** 2:
        return 'TRIANGULO OBTUSANGULO'
    else:
        return 'TRIANGULO ACUTANGULO'
    

def ordenar_decrescente(a, b, c):
    if a < c:
        auxiliar = a
        a = c
        c = auxiliar

    if b < c:
        auxiliar = b
        b = c
        c = auxiliar 

    if a < b:
        auxiliar = a
        a = b
        b = auxiliar       
    return a, b, c      


def main():
    valores = input().split()
    a, b, c = valores
    a = float(a)
    b = float(b)
    c = float(c)
    
    valores_ordenados = ordenar_decrescente(a, b, c)
    a, b, c = valores_ordenados
    
    if forma_triangulo(a, b, c):
        tipo1 = obter_tipo1(a, b, c)
        print(tipo1)

        if a == b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or a == c or b == c:
            print('TRIANGULO ISOSCELES')
    else:
        print('NAO FORMA TRIANGULO')

main()