from utils import obterNumInt

def encontrarMaior(n1, n2):
    return n1 if n1 > n2 else n2 if n2 > n1 else n1


def encontrarMMC(n1, n2):
    maior = encontrarMaior(n1, n2)

    mmc = maior

    while mmc % n1 != 0 or mmc % n2 != 0:
        mmc += maior
    return mmc


def main():
    num1 = obterNumInt('Primeiro número: ')
    num2 = obterNumInt('Segundo número: ')
    mmc = encontrarMMC(num1, num2  )

    print(f'O MMC dos números {num1} e {num2} é {mmc}')


main()        
   