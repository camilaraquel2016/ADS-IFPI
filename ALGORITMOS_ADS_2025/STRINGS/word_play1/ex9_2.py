from utils_string import obter_uma_letra

def nao_tem_letra(letra_proibida, palavra):

    for letra in palavra:
        if letra == letra_proibida:
            return False

    return True


def exibir_palavras_sem_tal_letra(letra_proibida, arquivo):
    tot_palavras = 0
    tot_palavras_sem_tal_letra = 0

    for linha in arquivo:
        tot_palavras += 1
        palavra = linha.strip()
        if nao_tem_letra(letra_proibida, palavra):
            tot_palavras_sem_tal_letra += 1
            print(palavra)

    print(f'{tot_palavras_sem_tal_letra / tot_palavras * 100:.1f}% das palavras brasileiras não têm a letra "{letra_proibida}"')        


def main():
  arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")    
  letra_proibida = obter_uma_letra('Insira a letra que não deve estar presente: ')
  exibir_palavras_sem_tal_letra(letra_proibida, arquivo)

