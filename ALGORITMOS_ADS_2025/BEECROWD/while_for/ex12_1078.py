def exibir_tabuada(num):
    for multiplicador in range(1, 11):
        print(f'{multiplicador} x {num} = {multiplicador * num}')


def main():
    num = int(input())
    exibir_tabuada(num)

main()    