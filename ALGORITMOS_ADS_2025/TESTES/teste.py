# # from math import sqrt

# # def ehPrimo(num, divisor = 2):
# #     raizQuadrada = sqrt(num)
    
# #     if num < 2:
# #         return False

# #     if divisor > raizQuadrada:
# #         return True

# #     if num % divisor != 0:
# #         return ehPrimo(num, divisor + 1)
    
# #     return False


# # def main():
# #     num = int(input("Número: "))
    
# #     if ehPrimo(num, 2):
# #         print(f"O número {num} é primo")
# #     else:
# #         print(f"O número {num} não é primo")


# # main()


# # range é uma função que cria uma sequência de números, que pode ser percorrida com o laço for.,
# # Lista numérica:,
# # Exemplos de uso do range com uma, duas e três expressões:,
# # range(5),
# # Apenas um valor é passado: 5 é o valor final (não incluso).,
# # O início é 0 (padrão) e o passo é 1 (padrão).,
# # Resultado: 0, 1, 2, 3, 4,
# # range(5, 10),
# # Dois valores: 5 é o valor inicial, 10 é o valor final (não incluso).,
# # O passo ainda é 1 (padrão).,
# # Resultado: 5, 6, 7, 8, 9,
# # range(5, 10, 2),
# # Três valores: 5 é o início, 10 é o fim (não incluso), e 2 é o passo.,
# # Resultado: 5, 7, 9

# def nao_eh_0_ou_1(num):
#     return num != 0 and num != 1


# def filtrar(colecao, criterio):
#     nova_colecao = []

#     for item in colecao:
#         if criterio(item):
#             nova_colecao.append(item)

#     return nova_colecao
        

# def obter_qtd_chamadas(fibonacci):
#     qtd_chamadas = 1

#     if fibonacci == 0 or fibonacci == 1:
#         return qtd_chamadas
    
#     lista_atual = [fibonacci]
    
#     while True:
#         lista_auxiliar = []

#         if len(lista_atual) == 0:
#             return qtd_chamadas
        
        
#         for item in lista_atual:
#             lista_auxiliar.append(item - 1)
#             lista_auxiliar.append(item - 2)

#         # print(lista_atual) 
#         # print(lista_auxiliar)

#         qtd_chamadas += len(lista_auxiliar)
#         lista_atual = filtrar(lista_auxiliar, nao_eh_0_ou_1) 
#         # print(qtd_chamadas)

# print(obter_qtd_chamadas(int(input())))






# def somar_bits(bit1, bit2):
#     vai_um = 0

#     bit_resultado = ''
#     for i in range(5):

#         soma_da_vez = bit1[i] + bit2[i] + vai_um
#         if soma_da_vez == 1:
#             resultado_vez = 1
#         elif soma_da_vez == 0:
#             resultado_vez = 0
#         elif soma_da_vez == 10:
#             resultado_vez = 0
#             vai_um = 1   

#         bit_resultado = bit_resultado + ''

#     return bit_resultado   
# 
# 
#  
import os
def limpar_tela():
    os.system('cls')
    


def exibir_boas_vindas():
    print('\n' + '=' * 50)
    print('🎮 Bem-vindo(a) ao'.center(50))
    print('🧠  PLAY NUMBERS  🧠'.center(50))
    print('=' * 50 + '\n')

    nome = input('👤 Qual o seu nome? ')
    
    limpar_tela()

    print('\n' + '=' * 50)
    print(f'🤝 Prazer em ter você aqui, {nome}!'.center(50))
    print('=' * 50 + '\n')

    print('📌 Antes de executar o programa, preciso saber quais serão os valores usados para manipulação.')
    print('📊 Por favor, analise o menu abaixo e escolha a melhor opção.\n')
    input('👉 Pressione Enter para continuar...')
    limpar_tela()

    # vetor, nome_do_arquivo = inicializar_vetor_numerico()

    # print('\n✅ Vetor inicializado com sucesso!')
    # print(f'📁 Arquivo: {nome_do_arquivo}')
    # print(f'📦 Valores carregados: {vetor}\n')
exibir_boas_vindas()