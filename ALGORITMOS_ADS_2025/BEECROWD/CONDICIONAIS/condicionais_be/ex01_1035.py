def eh_positivo(num):
    return num > 0


def eh_par(num):
    return num % 2 == 0


def sao_valores_aceitos(a, b, c, d):
    soma_a_b = a + b
    soma_c_d = c + d

    return b > c and d > a and soma_c_d > soma_a_b and eh_positivo(c) and eh_positivo(d) and eh_par(a)


def main():
    valores = input().split()
    a = int(valores[0])
    b = int(valores[1])
    c = int(valores[2])
    d = int(valores[3])
    
    if sao_valores_aceitos(a, b, c, d):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')    
    
main()