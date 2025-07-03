def eh_maiscula(caractere):
    codigo = ord(caractere)
    return codigo >= 65 and codigo <= 90


def avancar_posicoes(caractere, qtd_posicoes):
    novo_codigo = ord(caractere) + qtd_posicoes

    return chr(novo_codigo)


def converter_para_minusculo(texto):
    novo_texto = ''

    for caractere in texto:

        if eh_maiscula(caractere):
            caractere = avancar_posicoes(caractere, 32)

        novo_texto += caractere  

    return novo_texto      





def eh_letra(caractere):
    codigo = ord(caractere)

    return (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)


def obter_uma_letra(label):
    while True:
        caractere = input(label)

        if len(caractere) == 1:
            if eh_letra(caractere):
                return caractere

        print('Entrada invalida!\nO caractere inserido deve ser uma letra e somente uma')    


def obter_num_inteiro(label):
    while True:
        try:
            num = int(input(label))
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número inteiro')


def exibir_palavras(palavras):
    for palavra in palavras:
        print(palavra)
    

def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item )

    return nova_colecao        


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao
    

def carregar_palavras():
    palavras = mapear(open(r"C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\FOR\word_play.2\br-sem-acentos.txt").readlines(), lambda x:x.strip())
    return mapear(palavras, converter_para_minusculo)


