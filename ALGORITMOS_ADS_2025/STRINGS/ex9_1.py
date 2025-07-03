from utils_string import obter_inteiro

def tem_mais_de_n_carac(palavra, n): #palavra deve ser inserida sem espaços em brancos
        return len(palavra) > n


def exibir_palavras_com_mais_de_n_caractere(arquivo, n):
    total_palavra = 0
    total_palavra_mais_de_n = 0


    for linha in arquivo:
        palavra = linha.strip()
        total_palavra += 1

        if tem_mais_de_n_carac(palavra, n):
             total_palavra_mais_de_n += 1
             print(palavra)

    print(f'{total_palavra_mais_de_n / total_palavra * 100:.3f}% das palavras brasileiras tem mais de {n} caracteres em sua composição')         

        
def main():
    arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")    
    n = obter_inteiro('N caracteres: ')
    exibir_palavras_com_mais_de_n_caractere(arquivo, n)

if __name__ == "__main__":
    main()

     


    
    

