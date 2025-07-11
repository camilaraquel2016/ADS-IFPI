def substituir(num):
    return 1 if num <= 0 else num


def repetir(qtd_vezes):
    for vez in range(qtd_vezes):
        num = substituir(int(input()))
        print(f'X[{vez}] = {num}')


def main():
    repetir(10)

main()    