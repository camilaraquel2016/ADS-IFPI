def eh_primo(num):
    if num < 2:
        return False
    
    raizQuadrada = num ** 0.5
    limiteFinal = int(raizQuadrada) + 1

    for divisor in range(2, limiteFinal, 1):
        if num % divisor == 0:
            return False

    return True


def exibir_primos(limite_inicial, limite_final):
    limite_final += 1
    for i in range(limite_inicial, limite_final, 1):
        if eh_primo(i):
            print(i)

         
def main():
    limite_inicial = int(input('Limite inicial: '))
    limite_final = int(input('Limite final: '))

    exibir_primos(limite_inicial, limite_final)

main()
