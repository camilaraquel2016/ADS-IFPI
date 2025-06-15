def obter_maior_quadrado(num):
    return int(num ** 0.5) ** 2


def main():
    num = int(input('Número: '))
    maior_quadrado = obter_maior_quadrado(num)
    print(f'Maior quadrado: {maior_quadrado}')

main()    