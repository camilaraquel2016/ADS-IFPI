def filtrar(colecao, funcao_criterio):
    nova_colecao = []

    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)

    return nova_colecao        


def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao


def eh_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


def obter_tipo_do_triangulo(a, b, c):
    if a == b == c:
        return 'Equilatero'
    elif a != b and b != c and a != c:
        return 'Escaleno'
    else:
        return 'Isoceles'
    

def eh_triangulo_retangulo(a, b, c):
    hipotenusa = reduzir([a, b, c], obter_maior, a)

    try:
        cateto1, cateto2 = filtrar([a, b, c], lambda x: x < hipotenusa)
        return hipotenusa ** 2 == cateto1 ** 2 + cateto2 ** 2
    except ValueError:
        return False



def main():
    a, b, c = mapear(input().split(), int)

    if eh_triangulo(a, b, c):
        tipo_do_triangulo = obter_tipo_do_triangulo(a, b, c)
        resposta_retangulo = 'S' if eh_triangulo_retangulo(a, b, c) else 'N'
        print(f'Valido-{tipo_do_triangulo}')
        print(f'Retangulo: {resposta_retangulo}')
    else:
        print('Invalido')

main()            




