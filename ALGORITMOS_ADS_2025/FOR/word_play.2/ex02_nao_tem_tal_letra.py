from utils import obter_uma_letra, filtrar, exibir_palavras, carregar_palavras, converter_para_minusculo

def nao_tem_letra_proibida(letra_proibida, palavra):
    for letra in palavra:
        if letra == letra_proibida:
            return False
        
    return True    


def exibir_palavras_sem_letra_proibida(letra_proibida, palavras):
    palavras_sem_letra_proibida = filtrar(palavras, lambda palavra: nao_tem_letra_proibida(letra_proibida, palavra))
    exibir_palavras(palavras_sem_letra_proibida)

    qtd_palavras_sem_filtro = len(palavras)
    qtd_palavras_com_filtro = len(palavras_sem_letra_proibida)

    print(f'{qtd_palavras_com_filtro / qtd_palavras_sem_filtro * 100:.3f}% das palavras não tem a letra "{letra_proibida}" em sua composição')


def main():
    palavras = carregar_palavras()
    letra_proibida = converter_para_minusculo(obter_uma_letra('Insira a letra proibida: '))
    exibir_palavras_sem_letra_proibida(letra_proibida, palavras)
    

if __name__ == '__main__':
    main()





