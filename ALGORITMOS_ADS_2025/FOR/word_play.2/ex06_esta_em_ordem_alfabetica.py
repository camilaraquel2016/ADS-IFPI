from utils import carregar_palavras, filtrar, exibir_palavras

def esta_em_ordem_alfabetica(palavra): # antes de executar deve garantir que o pametro terá o mesmo padrão ex: todas maíusculas ou todas minúsculas
    codigo_anterior = 0

    for letra in palavra:
        codigo_atual = ord(letra)
        if codigo_atual < codigo_anterior:
            return False
        
        codigo_anterior = codigo_atual

    return True    


def exibir_palavras_em_ordem_alfabetica(palavras):
    palavras_em_ordem_alfabetica = filtrar(palavras, esta_em_ordem_alfabetica)
    exibir_palavras(palavras_em_ordem_alfabetica)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_em_ordem_alfabetica)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras estão em ordem alfabética')


def main():
    palavras = carregar_palavras()
    exibir_palavras_em_ordem_alfabetica(palavras)


if __name__ == '__main__':
    main()    
