def eh_perfeito(num):
    soma_divisores = 0

    for d in range(1, num, 1):
        if num % d == 0:
            soma_divisores += d

    return soma_divisores == num        


def main():
    num = int(input('Número: '))
    
    if eh_perfeito(num):
        print(f'O número {num} é perfeito')
    else:
        print(f'O número {num} não é perfeito')

main()
