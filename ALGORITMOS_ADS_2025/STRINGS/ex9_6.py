from utils_string import converter_maisculo

def esta_em_ordem_alfabetica(palavra):
    palavra = converter_maisculo(palavra)
    letra_anterior = palavra[0]
   
    for index in range(1, len(palavra), 1):
        letra_atual = palavra[index]

        if letra_anterior > letra_atual:
            return False
        
        letra_anterior = letra_atual
    
    return True    


def exibir_palavras_em_ordem_alfabetica(arquivo):
    total_palavra = 0
    total_palavra_em_ordem = 0

    for linha in arquivo:
        palavra = converter_maisculo(linha.strip())
        total_palavra += 1

        if esta_em_ordem_alfabetica(palavra):
            total_palavra_em_ordem += 1
            print(palavra)

    print(f'{total_palavra_em_ordem / total_palavra * 100:.3f}% das palavras estão em ordem alfabética') 


def main():
    arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")
    
    exibir_palavras_em_ordem_alfabetica(arquivo)

   


