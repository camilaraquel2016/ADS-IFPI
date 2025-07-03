from utils import filtrar, exibir_palavras, carregar_palavras, obter_num_inteiro

def tem_mais_de_n_caractere(palavra, n):
    return len(palavra) > n


def exibir_palavras_com_mais_de_n_caracteres(n, palavras):
    palavras_com_mais_de_n_caracteres = filtrar(palavras, lambda x: len(x) > n)
    exibir_palavras(palavras_com_mais_de_n_caracteres)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_com_mais_de_n_caracteres)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras tem mais de {n} caracteres em sua composição')


def main():
    palavras = carregar_palavras()
    n = obter_num_inteiro('N caracteres: ')
    exibir_palavras_com_mais_de_n_caracteres(n, palavras)


if __name__ == '__main__':
    main()    
