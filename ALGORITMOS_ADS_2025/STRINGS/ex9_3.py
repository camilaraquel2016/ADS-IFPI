from utils_string import converter_maisculo, eh_letra

def obter_letra(label: str):
    
    while True:
        caractere = converter_maisculo(str(input(label)))

        if caractere == 'PARAR':
            return caractere
        
        if len(caractere) == 1:
            if eh_letra(caractere):
                return caractere
        
        print('Entrada inválida!\nVocê deve inserir somente um caractere por vez e esse caractere deve ser uma letra')


def obter_letras_proibidas(): # retorna uma string com as junções das letras proibidas
    letras_proibidas = ''
    contador = 1

    while True:
        letra = obter_letra(f'{contador}° letra proibida: (flag = PARAR) ')

        if letra == 'PARAR':
            return letras_proibidas
        
        letras_proibidas += letra
        contador += 1


def tem_letra_proibida(letras_proibidas, palavra):
    for letra in palavra:
        for letra_proibida in letras_proibidas:
            if letra == letra_proibida:
                return True

    return False        


def exibir_palavras_sem_letras_proibidas(letras_proibidas, arquivo):
    total_palavras = 0
    total_palavras_sem_letras_proibidas = 0

    for linha in arquivo:
        palavra = converter_maisculo(linha.strip())
        total_palavras += 1

        if not tem_letra_proibida(letras_proibidas, palavra):
            total_palavras_sem_letras_proibidas += 1
            print(palavra)

    print(f'{total_palavras_sem_letras_proibidas / total_palavras * 100:.3f}% das palavras brasileiras não tem as letras "{letras_proibidas}" em sua composição')        


def main():
    letras_proibidas = obter_letras_proibidas()    
    arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")

    exibir_palavras_sem_letras_proibidas(letras_proibidas, arquivo)


