from utils import mapear, converter_para_minusculo, carregar_palavras, filtrar, exibir_palavras

def esta_na_lista(lista, caratere):
    for item in lista:
        if item == caratere:
            return True

    return False     


def nao_tem_letras_proibidas(letras_proibidas, palavra):
    for letra in palavra:
        if esta_na_lista(letras_proibidas, letra):
            return False
        
    return True    


def exibir_palavras_sem_letras_proibidas(letras_proibidas, palavras):
    palavras_sem_letras_proibidas = filtrar(palavras, lambda palavra: nao_tem_letras_proibidas(letras_proibidas, palavra))
    exibir_palavras(palavras_sem_letras_proibidas)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_sem_letras_proibidas)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras não possuem as letras "{letras_proibidas}" em sua composição')


def main():
    palavras = carregar_palavras()
    letras_proibidas = mapear(input('Insira as letras proibidas: '), converter_para_minusculo)
    exibir_palavras_sem_letras_proibidas(letras_proibidas, palavras)


if __name__ == '__main__':
    main()
    
