from time import sleep
from utils import obterNumInt, limparTela

def saidaNumErrado():
    print(' ')
    sleep(1)
    print('NÚMERO ERRADO!')
    print(' ')
    sleep(1)


def advinharNum(num):
    while True:
        numCanditado = obterNumInt('Vamos encontrar o número inicial...\nQual seu palpite? ')
        if numCanditado == num:
            break
        else:
            saidaNumErrado()
            
    return f'Você acertou!\nO número que estávamos tentando advinhar é o {num}'


def main():
    num = obterNumInt('Insira um número qualquer: ')
    limparTela()
    print(advinharNum(num))   

main()    





