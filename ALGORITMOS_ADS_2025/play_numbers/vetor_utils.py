from random import uniform, randint
from utils import *

def boas_vindas():
    limpar_tela()
    msg = '''
    -=-=-=-=-🎮 Seja bem-vindo(a) ao Play Numbers 🎮-=-=-=-=-

      O Play Numbers é um programa bastante interativo
      e cheio de funcionalidades, fique a vontade para 
      explorar as mais diversas manipulações de vetores

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
    print(msg)
    input(' \nEnter para continuar...')
    limpar_tela()


# FUNCOES CRITERIO
   
def eh_positivo(num):
    return num > 0


def eh_negativo(num):
    return num < 0


# FUNCOES REDUTORAS

def somar(n1, n2):
    return n1 + n2


def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


def obter_menor(n1, n2):
    return n1 if n1 < n2 else n2


# FUNCOES PEDIR ENTRADA ESPECIFICA    

def obter_resposta(label: str, opcao1: str, opcao2: str):
    while True:
        resposta = input(label).upper()

        if resposta == opcao1 or resposta == opcao2:
            return resposta
        
        print(f'Resposta inválida!\nO valor inserido deve ser "{opcao1}" ou "{opcao2}"')


# FUNCOES DE MENU

def menu_alterar_valores():
    return f'''
    -=-REGRAS DE ALTERAÇÃO-=-
       1 - Multiplicar por um valor
       2 - Elevar a um valor
       3 - Reduzir a uma fração 
       4 - Substituir valores negativos por um número aleatório
       5 - Ordenar valores
       6 - Embaralhar valores

       0 - Sair

       >>> '''


def menu_inicializar():
    return f'''
    1 - Gerar vetor de forma (automática)
    2 - Gerar vetor de forma (manual)

    >>> '''


def menu_gerar_manual():
    return f'''
    1 - Carregar o vetor de um arquivo
    2 - Inserir valores para criar o vetor

    >>> '''


def exibir_arquivos_exemplos():
    return f'''
    ARQUIVOS DISPONÍVEIS

    1 - nuvem_numerica.txt
    2 - explosao_de_valores.txt
    3 - caixa_de_dados.txt
    4 - chuva_de_numeros.txt
    5 - vetor_fantasma.txt

    >>> '''


# FUNCOES GERAR VETOR 

def criar_vetor_manualmente(tamanho_do_vetor, limite_min, limite_max):
    vetor = []

    for insercao in range(1, tamanho_do_vetor + 1): 
        vetor.append(obter_num_real_na_faixa(f'Insira o {insercao}° número: ', limite_min, limite_max))

    return vetor    


def gerar_vetor_aleatorio(tamanho_do_vetor: int, limite_min: float, limite_max: float):
    vetor = []

    for _ in range(tamanho_do_vetor):
        vetor.append(round(uniform(limite_min, limite_max), 2))

    return vetor    


def carregar_vetor_do_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo).readlines()
    return mapear(arquivo, lambda x: float(x.strip()))


# FUNCOES RELACIONADAS A ARQUVOS 

def obter_nome_do_arquivo(opcao_arquivo):
    nome_dos_arquivos = ['nuvem_numerica', 'explosao_de_valores', 'caixa_de_dados', 'chuva_de_numeros', 'vetor_fantasma'] 
    posicao = opcao_arquivo - 1

    return nome_dos_arquivos[posicao]


def obter_caminho_do_arquivo(nome_do_arquivo):
    return rf'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\play_numbers\{nome_do_arquivo}.txt'


# FUNCOES MAPEAR, FILTRAR, REDUZIR

def mapear(vetor, funcao_transformadora):
    novo_vetor = []

    for item in vetor:
        novo_vetor.append(funcao_transformadora(item))
        
    return novo_vetor

        
def filtrar(vetor, funcao_criterio):
    novo_vetor = []

    for item in vetor:
        if funcao_criterio(item):
            novo_vetor.append(item)

    return novo_vetor


def reduzir(vetor, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in vetor:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


####

def eh_posicao_valida(posicao: int, lista: list):
    try:
        lista[posicao]
        return True
    except IndexError:
        return False


def embaralhar_valores(vetor, qtd_embaralhamentos):
    qtd_posicoes = len(vetor)

    for embaralhamento in range(qtd_embaralhamentos):
        pos_sorteada_1 = randint(0, qtd_posicoes - 1)
        pos_sorteada_2 = randint(0, qtd_posicoes - 1)
        vetor[pos_sorteada_1], vetor[pos_sorteada_2] = vetor[pos_sorteada_2], vetor[pos_sorteada_1]

    return vetor    
