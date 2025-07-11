def tem_ponto_final(simbolo):
    return simbolo[len(simbolo) - 1] == '.'


def eh_palavra(simbolo):
    for caractere in simbolo:
        if caractere < 'A' or caractere > 'Z':
            return False

    return True    


def obter_tamanho_medio(texto):
    texto = texto.split()
    
    qtd_palavras = 0
    total_letras = 0

    for simbolo in texto:
        if tem_ponto_final(simbolo):
            simbolo = simbolo[0:-1]
        if eh_palavra(simbolo):
            total_letras += len(simbolo)
            qtd_palavras += 1

    return total_letras / qtd_palavras if qtd_palavras > 0 else 0        
            

def obter_qtd_pontos(texto):
    comprimento_medio_palavra = int(obter_tamanho_medio(texto))
    if comprimento_medio_palavra <= 3:
        return 250
    elif comprimento_medio_palavra <= 5:
        return 500
    else:
        return 1000


def main():
    try:
        while True:
            texto = input().upper()
            if not texto:
                continue

            qtd_de_pontos = obter_qtd_pontos(texto)
            print(qtd_de_pontos)

    except EOFError:
        pass        


main()