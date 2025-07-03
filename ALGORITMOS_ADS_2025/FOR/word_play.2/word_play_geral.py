import os
from utils import obter_num_inteiro, carregar_palavras, obter_uma_letra, mapear, converter_para_minusculo
from ex01_mais_de_n import exibir_palavras_com_mais_de_n_caracteres
from ex02_nao_tem_tal_letra import exibir_palavras_sem_letra_proibida
from ex03_sem_letras_proibidas import exibir_palavras_sem_letras_proibidas
from ex04_letras_permitidas import exibir_palavras_com_letras_permitidas
from ex05_usa_letras_obrigatorias import exibir_palavras_com_letras_obrigatorias
from ex06_esta_em_ordem_alfabetica import exibir_palavras_em_ordem_alfabetica

def esta_na_lista(caractere, lista):
    for item in lista:
        if item == caractere:
            return True

    return False    


def obter_opcao(label):
    opcoes_disponiveis = [0, 1, 2, 3, 4, 5, 6]

    while True:
        opcao = obter_num_inteiro(label)

        if esta_na_lista(opcao, opcoes_disponiveis):
            return opcao
        
        print('Opção inválida!')


def menu():
    return f'''
    |<<<<<<<< WORD PLAY >>>>>>>|

    1 - Palavras com mais de N caracteres
    2 - Palavras sem a letra proibida
    3 - Palavras sem letras proibidas
    4 - Palavras com letras permitidas
    5 - Palavras com letras obrigatórias
    6 - Palavras que seguem a ordem alfabética

    0 - Sair

    >>> '''


def main():
    print('Iniciando programa...')
    palavras = carregar_palavras()

    while True:
        opcao = obter_opcao(menu())

        match opcao:
            case 1:
                n = obter_num_inteiro('N caractere: ')
                exibir_palavras_com_mais_de_n_caracteres(n, palavras)
            case 2:
                letra_proibida = obter_uma_letra('Letra proibidida: ')
                exibir_palavras_sem_letra_proibida(letra_proibida, palavras)
            case 3:
                letras_proibidas = mapear(input('Insira as letras proibidas: '), converter_para_minusculo)
                exibir_palavras_sem_letras_proibidas(letras_proibidas, palavras)
            case 4:
                letras_permitidas = mapear(input('Insira as letras permitidas: '), converter_para_minusculo)
                exibir_palavras_com_letras_permitidas(letras_permitidas, palavras)
            case 5:
                letras_obrigatorias = mapear(input('insira as letras obrigatórias: '), converter_para_minusculo)
                exibir_palavras_com_letras_obrigatorias(palavras, letras_obrigatorias)
            case 6:
                exibir_palavras_em_ordem_alfabetica(palavras)    
            case 0:
                print('Encerrando programa...')    
                break


        continuar = input('Enter para continuar ')  
        os.system('cls')  


if __name__ == '__main__':
    main()
          
            

