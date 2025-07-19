def criar_lista(qtd_itens):
    lista_de_itens = []

    for item in range(qtd_itens):
        lista_de_itens.append(input())

    return lista_de_itens


def main():
    try:
        while True:
            qtd_livros = int(input())
            if not qtd_livros:
                break
            
            lista_de_codigos = criar_lista(qtd_livros)
            lista_ordenada = sorted(lista_de_codigos)

            for codigo in lista_ordenada:
                print(codigo)
    except (EOFError, ValueError):
        pass
main()    