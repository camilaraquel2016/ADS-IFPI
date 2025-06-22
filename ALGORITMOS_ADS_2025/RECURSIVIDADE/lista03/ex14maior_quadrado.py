from utils import obterNumInteiro

def obter_maior_quadrado(num):
    resultado_real = num ** 0.5
    parte_inteira = int(resultado_real)

    if parte_inteira ** 2 == num:
        return num
    
    return obter_maior_quadrado(num - 1)


def main():
    num = obterNumInteiro('Insira um número: ')
    maior_quadrado = obter_maior_quadrado(num)

    print(f'O maior quadrado é {maior_quadrado}')

main()    