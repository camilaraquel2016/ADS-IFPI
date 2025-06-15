from utils import obterNumInt

def encontraQtdDig(num):
    contador = 1
    qtdDig = 0

    while contador <= num:
        contador *= 10
        qtdDig += 1

    return qtdDig

def main():
    num = obterNumInt('Número que deseja analisar: ')
    qtdDig = encontraQtdDig(num)
    print(f'O número {num} é composto por {qtdDig} dígito(s)')

main()    




        
