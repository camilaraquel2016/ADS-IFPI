def formatar_num(num):
    num = float(f'{num:.1f}')

    if num == int(num):
        return int(num) 
    return num


def obter_saida(i, j):
    j = formatar_num(j)
    i = formatar_num(i)
    return f'I={i} J={j}'


def exibir_sequencia():
    i, j = 0, 1
    while i <= 2:
        contador_j = 1
        j = i + 1
        while contador_j <= 3:
            print(obter_saida(i, j))
            j += 1
            contador_j += 1
        i += 0.2    


def main():
    exibir_sequencia()           

main()