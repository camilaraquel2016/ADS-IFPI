def eh_par(num):
    return num % 2 == 0


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao        


def repetir(num):
    numeros_pares = filtrar(range(1, num + 1), eh_par)

    for num_par in numeros_pares:
        print(f'{num_par}^2 = {num_par ** 2}')


def main():
    num = int(input())   
    repetir(num) 

main()    