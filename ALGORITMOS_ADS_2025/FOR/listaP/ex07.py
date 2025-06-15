def somar_intervalo(limite_final):
    soma = 0
    limite_final += 1

    for num in range(1, limite_final, 1):
        soma += num

    return soma    


def main():
    limite_final = int(input('Limite final: '))
    soma = somar_intervalo(limite_final)
    print(f'A soma do intervalo (1 a {limite_final}) é igual a {soma}')

main()