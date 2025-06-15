def obter_primeiro_multiplo(num, limite_inicial):
    limite_final = limite_inicial + 1

    for i in range(1, limite_final, 1):
        multiplo = num * i
        if multiplo >= limite_inicial:
            return multiplo


def exibir_multiplos(limite_inferior, limite_superior, num):
    primeiro_multiplo = obter_primeiro_multiplo(num, limite_inferior)
    limite_superior += 1

    for i in range(primeiro_multiplo, limite_superior, num):
        print(i)


def main():
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))        
    num = int(input('Número: '))
    print(f'-=-MÚLTIPLOS DE {num} NO INTERVALO ({limite_inferior} A {limite_superior})-=-')
    exibir_multiplos(limite_inferior, limite_superior, num)

main()    




