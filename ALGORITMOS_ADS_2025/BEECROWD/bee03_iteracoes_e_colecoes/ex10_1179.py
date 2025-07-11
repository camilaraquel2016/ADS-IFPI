def exibir_lista(lista, tipo):  
    posicao = 0  

    for item in lista:
        print(f'{tipo}[{posicao}] = {item}')
        posicao += 1


def obter_qtd_listas(lista):
    tamanho_lista = len(lista)
    resto = tamanho_lista % 5

    return tamanho_lista // 5 if resto == 0 else tamanho_lista // 5 + 1


def exibir_formatacao(lista_pares, qtd_listas_pares, lista_impares, qtd_listas_impares):
    tamanho_lista_par = len(lista_pares)
    tamanho_lista_impar = len(lista_impares)

    exibir_primeiro = lista_pares[0: 5]
    exibir_lista(exibir_primeiro, 'par')
    
    

    

def obter_lista(qtd_entradas):
    lista = []

    for entrada in range(qtd_entradas):
        entrada = int(input())
        lista.append(entrada)

    return lista    


def eh_par(num):
    return num % 2 == 0


def eh_impar(num):
    return num % 2 == 1


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao        


def main():
    qtd_entradas = 15
    lista = obter_lista(qtd_entradas)

    lista_pares = filtrar(lista, eh_par)
    qtd_listas_pares = obter_qtd_listas(lista_pares)

    lista_impares = filtrar(lista, eh_impar)
    qtd_listas_impares = obter_qtd_listas(lista_impares)

    exibir_formatacao(lista_pares, qtd_listas_pares, lista_impares, qtd_listas_impares)
main()