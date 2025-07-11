def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


def ajustar_formatacao(colecao):
    tamanho_do_maior_nome = reduzir(colecao, lambda maior, nome: obter_maior(maior, len(nome)), 0)
    
    for nome in colecao:
        qtd_espacos_necessarios = lambda nome, tamanho_do_maior_nome: tamanho_do_maior_nome - len(nome)
        espaco_necessario = ' ' * qtd_espacos_necessarios(nome, tamanho_do_maior_nome) 
        print(f'{espaco_necessario}{nome}')


def obter_lista(qtd_elementos):
    lista = []

    for entrada in range(qtd_elementos):
        lista.append(input())

    return lista     


def main():
    qtd_nomes = int(input())

    while qtd_nomes != 0:

        lista_de_nomes = obter_lista(qtd_nomes)  
        ajustar_formatacao(lista_de_nomes)

        qtd_nomes = int(input())
        
        if qtd_nomes != 0:
            print()

main()    

    