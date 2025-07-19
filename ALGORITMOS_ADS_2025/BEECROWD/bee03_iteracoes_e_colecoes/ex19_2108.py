def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao
    

def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    


def exibir_saida(lista, sinal_de_separacao: str):
    saida = ''

    for item in lista:
        saida += f'{item}{sinal_de_separacao}'

    return saida.strip(sinal_de_separacao)            


def processar_dados():
    maior_palavra = ''

    while True:
        frase = input()

        if frase == '0':
            print('')
            print(f'The biggest word: {maior_palavra}')
            break

        frase = frase.split()    
        lista_de_qtd_de_letras = mapear(frase, lambda palavra: len(palavra))
        maior_palavra = reduzir(frase, lambda x, y: x if len(x) > len(y) else y, maior_palavra)
        print(exibir_saida(lista_de_qtd_de_letras, '-'))
        

def main():
    processar_dados()

main()



