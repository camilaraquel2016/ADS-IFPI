from utils import obterNumReal

def divisores(x, n):

    while n >= 2:
        resultado = x / n
        print(f'{x:.2f} / {n:.2f} = {resultado:.2f}')
        x = resultado
        n -= 1

def main():
    x = obterNumReal('Valor de x: ')
    n = obterNumReal('Valor de n: ')

    divisores(x, n)

main()    
