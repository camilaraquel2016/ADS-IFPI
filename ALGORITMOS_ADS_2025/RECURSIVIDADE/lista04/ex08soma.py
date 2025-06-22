from utils import obterNumInteiro
import os

def somar_e_encontrar_num(num_escolhido, antecessor):
    num_atual = obterNumInteiro('Insira um número: ')

    resultado = antecessor + num_atual

    if resultado == num_escolhido:
        return f'Número encontrado!!!\n{antecessor} + {num_atual} = {resultado}'
    
    antecessor = num_atual
    return somar_e_encontrar_num(num_escolhido, antecessor)


def main():
    num_escolhido = obterNumInteiro('Insira um número: ')
    os.system('cls')
    primeiro_num = obterNumInteiro('Insira um número: ')
    print(somar_e_encontrar_num(num_escolhido, primeiro_num))

main()    


    
