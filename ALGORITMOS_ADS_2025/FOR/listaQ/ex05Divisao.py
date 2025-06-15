from utils import obter_inteiro_positivo


def exibir_divisoes(x, n):

    for i in range(n, 1, -1):
        resultado = x / i
        print(f'{resultado:.2f}')
        
        x = resultado




def main():
    x = obter_inteiro_positivo('X: ')
    n = obter_inteiro_positivo('N: ')
    exibir_divisoes(x, n)

main()    
