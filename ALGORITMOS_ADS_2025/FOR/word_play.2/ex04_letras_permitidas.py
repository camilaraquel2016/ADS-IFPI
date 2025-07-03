from utils import mapear, converter_para_minusculo, carregar_palavras, filtrar, exibir_palavras

def esta_na_lista(lista, caractere):
    for item in lista:
        if item == caractere:
            return True

    return False    


def usa_somente_letras_permitidas(palavra, letras_permitidas):
    for letra in palavra:
        if not esta_na_lista(letras_permitidas, letra):
            return False

    return True    


def exibir_palavras_com_letras_permitidas(letras_permitidas, palavras):
    palavras_com_letras_permitidas = filtrar(palavras, lambda palavra:usa_somente_letras_permitidas(palavra, letras_permitidas))
    exibir_palavras(palavras_com_letras_permitidas)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_com_letras_permitidas)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras usam somente as letras "{letras_permitidas}" em sua composição')

    
def main():
    palavras = carregar_palavras()
    letras_permitidas = mapear(input('Letras permitidas: '), converter_para_minusculo)
    exibir_palavras_com_letras_permitidas(letras_permitidas, palavras)


if __name__ == '__main__':
    main()    