from utils import obter_inteiro_maior_que_0

def eh_impar(num):
    return num % 2 == 1


def somar_fracoes(n, numerador = 1, denominador = 1, soma = 0):

    if denominador <= n:
        resultado = numerador / denominador

        if eh_impar(denominador):
            soma += resultado

        else:
            soma -= resultado

        denominador += 1
        return somar_fracoes(n, 1, denominador, soma)

    return soma        
            

def main():
    n = obter_inteiro_maior_que_0('Valor de N: ')
    soma = somar_fracoes(n, 1, 1, 0)
    print(f'A soma é {soma:.2f}')

main()    

