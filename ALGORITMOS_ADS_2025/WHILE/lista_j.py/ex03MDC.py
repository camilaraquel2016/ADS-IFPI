from utils import obterNumInt

# 5 e 6 

def encontrarMenor(n1, n2):
    return n1 if n1 < n2 else n2 if n2 < n1 else n1


def encontraMDC(n1, n2):
    menor = encontrarMenor(n1, n2)
    contador = 1
    mdc = 1

    while contador <= menor:
        if n1 % contador == 0 and n2 % contador == 0:
            mdc = contador
        contador += 1
    return mdc    


def main():
    num1 = obterNumInt('Primeiro valor: ')
    num2 = obterNumInt('Segundo valor: ')

    mdc = encontraMDC(num1, num2)

    print(f'O MDC dos números {num1} e {num2} é {mdc}')

main()    


