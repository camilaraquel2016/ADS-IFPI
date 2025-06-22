from utils import obter_inteiro_maior_que_0

def obter_soma(n, denominador, numerador = 1, soma = 0):

    if numerador <= n:
        resultado = numerador / denominador
        soma += resultado
        numerador += 1
        denominador -= 1
        return obter_soma(n, denominador, numerador, soma)
    
    return soma


def main():
    n = obter_inteiro_maior_que_0('Valor de N: ')
    denominador = n
    soma = obter_soma(n, denominador, 1, 0)

    print(f'A soma é {soma}')

main()    

