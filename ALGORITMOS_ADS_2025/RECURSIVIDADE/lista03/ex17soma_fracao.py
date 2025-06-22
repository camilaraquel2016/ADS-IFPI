from utils import obter_inteiro_maior_que_0

def obter_soma(n, soma = 0, denominador = 1):
    numerador = 1

    if denominador <= n:
        resultado = numerador / denominador
        soma += resultado

        denominador += 1
        return obter_soma(n, soma, denominador)
    
    return soma


def main():
    n = obter_inteiro_maior_que_0('Valor de N: ')
    soma = obter_soma(n, 0, 1)
    print(f'A soma é {soma:.1f}')

main()    