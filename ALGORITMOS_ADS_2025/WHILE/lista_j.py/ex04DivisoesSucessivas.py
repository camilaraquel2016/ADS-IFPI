from utils import obterNumInt

def dividirSucessivamente(num):
    while num >= 2:
        num /= 2
                
    return num

# def dividirSucessivamente(num):
#     contador = num
#     while contador >= 1:
#         num = contador
#         contador /= 2
#     return num

def main():
    num = obterNumInt('Número: ')
    resultado = dividirSucessivamente(num)
    print(f'O resultado da última operação é {resultado}')

main()    