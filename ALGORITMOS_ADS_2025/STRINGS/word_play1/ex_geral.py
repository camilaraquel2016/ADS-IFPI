from utils_string import obter_inteiro_na_faixa, obter_inteiro
from ex9_1 import exibir_palavras_com_mais_de_n_caractere
from ex9_2 import exibir_palavras_sem_tal_letra, obter_uma_letra
from ex9_3 import exibir_palavras_sem_letras_proibidas, obter_letras_proibidas
from ex9_4 import exibir_palavras_com_letras_permitidas, obter_letras_permitidas
from ex9_5 import exibir_palavras_com_letras_obrigatorias, obter_letras_obrigatorias
from ex9_6 import exibir_palavras_em_ordem_alfabetica

def menu():

      return obter_inteiro_na_faixa('''
      |>>>>>>>>>>>>>>>>>>>>> WordPLAY <<<<<<<<<<<<<<<<<<<<<|
       1 - Palavras com Tamanho N+ 
       2 - Palavras sem Caracter Proibido 
       3 - Palavras sem Letras Proibidas 
       4 - Palavras somente com Letras Permitidas 
       5 - Palavras com Letras Obrigatórias 
       6 - Palavras com Letras em Ordem Alfabética 

       0 - Sair         
       >>> ''', 0, 6)


def exibir_escolha(opcao, arquivo):
      if opcao == 1:
            n = obter_inteiro_na_faixa('N: ', 1, 50)
            exibir_palavras_com_mais_de_n_caractere(arquivo, n)

      elif opcao == 2:
            letra_proibida = obter_uma_letra('Insira a letra que não deve estar presente: ')
            exibir_palavras_sem_tal_letra(letra_proibida, arquivo)

      elif opcao == 3:
            letras_proibidas = obter_letras_proibidas()
            exibir_palavras_sem_letras_proibidas(letras_proibidas, arquivo)

      elif opcao == 4:
            letras_permitidas = obter_letras_permitidas()
            exibir_palavras_com_letras_permitidas(letras_permitidas, arquivo)     

      elif opcao == 5:
            letras_obrigatorias = obter_letras_obrigatorias()
            exibir_palavras_com_letras_obrigatorias(arquivo, letras_obrigatorias)

      elif opcao == 6:   
            exibir_palavras_em_ordem_alfabetica(arquivo)   

      elif opcao == 0:
            print('Encerrando...')      


def main():
      arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")
      opcao = menu()
      exibir_escolha(opcao, arquivo)
      
main()

