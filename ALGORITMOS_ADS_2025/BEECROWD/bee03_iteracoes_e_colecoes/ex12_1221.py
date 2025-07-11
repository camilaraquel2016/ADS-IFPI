def eh_primo(num):
    if num < 2:
        return False
    
    raiz_quadrada = int(num ** 0.5)
    contador = 2

    while contador <= raiz_quadrada:
        if num % contador == 0:
            return False

        contador += 1

    return True 


def repetir(qtd_vezes):
    for vez in range(qtd_vezes):

        num = int(input())

        if eh_primo(num):
            print('Prime')
        else:
            print('Not Prime')    


def main():
    n = int(input())
    repetir(n)

main()