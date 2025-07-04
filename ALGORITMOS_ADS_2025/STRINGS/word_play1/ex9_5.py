from utils_string import esta_na_lista, eh_letra, converter_maisculo

def obter_letra(label: str): 

    while True:
        caractere = converter_maisculo(str(input(label)))

        if caractere == 'PARAR':
            return caractere
        
        if len(caractere) == 1:
            if eh_letra(caractere):
                return caractere
            
        print('Entrada inválida!\nVocê deve inserir um caractere por vez e esse caractere deve ser uma letra')    


def obter_letras_obrigatorias():
    letras_obrigatorias = ''
    contador = 1

    while True:
        letra = obter_letra(f'{contador}° letra obrigatória: (flag = PARAR) ')

        if letra == 'PARAR':
            return letras_obrigatorias
        
        letras_obrigatorias += letra
        contador += 1


def usa_todas_letras_obrigatorias(letras_obrigatorias, palavra):
    for letra in letras_obrigatorias:
        if not esta_na_lista(letra, palavra):
            return False

    return True    


def exibir_palavras_com_letras_obrigatorias(arquivo, letras_orbigatorias):
    total_palavras = 0
    total_palavras_com_letras_obrigatorias = 0

    for linha in arquivo:
        palavra = converter_maisculo(linha.strip())
        total_palavras += 1

        if usa_todas_letras_obrigatorias(letras_orbigatorias, palavra):
            print(palavra)
            total_palavras_com_letras_obrigatorias += 1

    print(f'{total_palavras_com_letras_obrigatorias / total_palavras * 100:.3f}% das palavras usam as letras "{letras_orbigatorias}" em sua composição') 


def main():
    arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")
    letras_obrigatorias = obter_letras_obrigatorias()

    exibir_palavras_com_letras_obrigatorias(arquivo, letras_obrigatorias)

 
    
