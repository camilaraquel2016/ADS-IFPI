def repetir(n):
    for caso in range(n):
        nome = input()
        if nome == 'Batmain':
            print('N')
        else:
            print('Y')    


def main():
    n = int(input())
    repetir(n)

main()    