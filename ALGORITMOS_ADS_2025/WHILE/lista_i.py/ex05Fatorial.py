from utils import obterNumInt, validarLimiteMin

def calcularFatorial(num):
    fatorial = 1

    while num >= 1:
        fatorial *= num
        num -= 1

    return fatorial


def main():
    label = 'Qual número deseja calcular o fatorial? '
    num = obterNumInt(label)
    num = validarLimiteMin(num, 0, label)
    
    fatorial = calcularFatorial(num)

    print(f'O fatorial de {num} é {fatorial}')


main()







