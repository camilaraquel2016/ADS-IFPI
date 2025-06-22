from utils import obterNumInteiro
import os

def encontrar_num(num_escolhido):
    num_da_vez = obterNumInteiro('Tente adivinhar o número\n>>> ')

    if num_escolhido == num_da_vez:
        return 'Muito bem!\nNúmero encontrado!'
    
    print('Que pena!\nEsse não é o número escolhido')
    return encontrar_num(num_escolhido)


def main():
    num_escolhido = obterNumInteiro('Insira um número: ')
    os.system('cls')
    print(encontrar_num(num_escolhido))

main()

