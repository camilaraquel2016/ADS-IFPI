def eh_par(num):
    return num % 2 == 0


def formatar_texto(texto):
    caractere_negrito = 0
    caractere_italico = 0
    texto_formatado = ''

    for caractere in texto:
        if caractere == '*':
            caractere = '<b>' if eh_par(caractere_negrito) else '</b>'
            caractere_negrito += 1
            
        elif caractere == '_':
            caractere = '<i>' if eh_par(caractere_italico) else '</i>'
            caractere_italico += 1

        texto_formatado += caractere    

    return texto_formatado       


def main():
    try:
        while True:
            texto = input()
            if not texto:
                continue

            texto_em_html = formatar_texto(texto)
            print(texto_em_html)

    except EOFError:
        pass        

main()