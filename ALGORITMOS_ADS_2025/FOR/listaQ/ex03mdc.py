from utils import obter_inteiro_positivo

def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


def obter_menor(n1, n2):
    return n1 if n1 < n2 else n2


#usando algoritmo de euclides
# from itertools import count
# def obter_mdc(n1, n2):
#     a = obter_maior(n1, n2) 
#     b = obter_menor(n1, n2) 

#     for i in count():
#         resto = a % b 
#         a = b 
#         b = resto 

#         if b == 0:
#             return a


def obter_mdc(n1, n2):
    menor = obter_menor(n1, n2)
    
    for divisor in range(1, menor + 1, 1):
        if n1 % divisor == 0 and n2 % divisor == 0:
            mdc = divisor

    return mdc         


def main():
    n1 = obter_inteiro_positivo('Primeiro número: ')
    n2 = obter_inteiro_positivo('Segundo número: ')
    mdc = obter_mdc(n1, n2)
    print(f'O MDC de ({n1}, {n2}) = {mdc}')

main()







        

