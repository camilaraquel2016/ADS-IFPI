def vogalOuConsoante(letra: str):
    vogais = 'AEIOU'
    consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'
    return 'vogal' if letra in vogais else 'consoante' if letra in consoantes else 'inválido'


def main():
    print('-=-ANALISADOR DE CARACTERE-=-')
    letra = str(input('Insira uma letra: ')).upper()[0]
    tipoLetra = vogalOuConsoante(letra)
    print(f'O caractere "{letra}" é {tipoLetra}')

main()    