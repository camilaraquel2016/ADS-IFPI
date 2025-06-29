def eh_negativo(num):
    return num < 0


def obter_delta(a, b, c):
    return b ** 2 - 4 * a * c 


def obter_raiz_quadrada(num):
    return num ** 0.5


def obter_raiz_1(a, b, delta):
    raiz_quadrada_do_delta = obter_raiz_quadrada(delta)
    return (- b + raiz_quadrada_do_delta) / (2 * a)


def obter_raiz_2(a, b, delta):
    raiz_quadrada_do_delta = obter_raiz_quadrada(delta)
    return (- b - raiz_quadrada_do_delta) / (2 * a)


def main():
    valores = input().split()
    a = float(valores[0])
    b = float(valores[1])
    c = float(valores[2])

    delta = obter_delta(a, b, c)

    if a == 0 or eh_negativo(delta):
        print('Impossivel calcular')
    else:    
        raiz_1 = obter_raiz_1(a, b, delta)
        raiz_2 = obter_raiz_2(a, b, delta)

        print(f'R1 = {raiz_1:.5f}')
        print(f'R2 = {raiz_2:.5f}')
        
main()

