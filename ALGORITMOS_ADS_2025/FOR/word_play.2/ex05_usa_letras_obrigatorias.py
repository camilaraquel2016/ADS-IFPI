from utils import carregar_palavras, converter_para_minusculo, mapear, filtrar, exibir_palavras

def esta_na_lista(caractere, lista):
    for item in lista:
        if caractere == item:
            return True

    return False    


def usa_todas_as_letras_obrigatorias(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if not esta_na_lista(letra, palavra):
            return False
        
    return True


def exibir_palavras_com_letras_obrigatorias(palavras, letras_obrigatorias):
    palavras_com_letras_obrigatorias = filtrar(palavras, lambda palavra: usa_todas_as_letras_obrigatorias(palavra, letras_obrigatorias))
    exibir_palavras(palavras_com_letras_obrigatorias)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_com_letras_obrigatorias)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras usam as letras "{letras_obrigatorias}" pelo menos uma vez em sua composição')
    

def main():
    palavras = carregar_palavras()
    letras_obrigatorias = mapear(input('Letras obrigatórias: '), converter_para_minusculo)
    exibir_palavras_com_letras_obrigatorias(palavras, letras_obrigatorias)
    

if __name__ == '__main__':
    main()    