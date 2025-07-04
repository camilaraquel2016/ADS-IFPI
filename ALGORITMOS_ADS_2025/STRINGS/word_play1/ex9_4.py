from utils_string import converter_maisculo, eh_letra

def obter_letra(label: str):

    while True:
        caractere = converter_maisculo(str(input(label)))

        if caractere == 'PARAR':
            return caractere
        
        if len(caractere) == 1:
            if eh_letra(caractere):
                return caractere
            
        print('Entrada inválida!\nVocê deve inserir um caractere por vez e esse caractere deve ser uma letra')    


def obter_letras_permitidas():
    letras_permitidas = ''
    contador = 1

    while True:
        letra = obter_letra(f'{contador}° letra permitida: (flag = PARAR) ')

        if letra == 'PARAR':
            return letras_permitidas
        
        letras_permitidas += letra

        contador += 1
        

def letra_esta_na_lista(letra, lista):
    for caractere in lista:
        if caractere == letra:
            return True
        
    return False    


def usa_apenas_letras_permitidas(letras_permitidas, palavra):
    for letra in palavra:
        if not letra_esta_na_lista(letra, letras_permitidas):
            return False
        
    return True    


def exibir_palavras_com_letras_permitidas(letras_permitidas, arquivo):
    total_palavras = 0
    total_palavras_com_letras_permitidas = 0


    for linha in arquivo:
        palavra = converter_maisculo(linha.strip())
        total_palavras += 1

        if usa_apenas_letras_permitidas(letras_permitidas, palavra):
            total_palavras_com_letras_permitidas += 1
            print(palavra)


    print(f'{total_palavras_com_letras_permitidas / total_palavras * 100:.3f}% das palavras brasileiras usam apenas as "{letras_permitidas}" em sua composição')


def main():
    arquivo = open(r"C:\Users\thali\OneDrive\Área de Trabalho\ALGORITMOS_ADS_2025\STRINGS\br-sem-acentos.txt")
    letras_permitidas = obter_letras_permitidas()

    exibir_palavras_com_letras_permitidas(letras_permitidas, arquivo)

