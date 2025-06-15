from utils import obterNumInt, validarLimiteMin

def calcularMedia(somaElementos, qtdElementos):
    return somaElementos / qtdElementos


def somarNumeros(qtdElementos):
    somatorio = 0
    contador = 1

    while contador <= qtdElementos:
        num = obterNumInt(f'{contador}° número: ')
        somatorio += num
        contador +=1
    return somatorio


def main():
    print('-=-Vamos descobrir a soma e média dos números-=-')
    qtdElementos = obterNumInt('Qual a quantidade de elementos? ')
    qtdElementos = validarLimiteMin(qtdElementos, 1, 'Qual a quantidade de elementos? ')

    somaDosElementos = somarNumeros(qtdElementos)
    media = calcularMedia(somaDosElementos, qtdElementos)

    print(f'A soma dos {qtdElementos} elementos é {somaDosElementos}')
    print(f'A média dos elementos é {media:.2f}')

main()






