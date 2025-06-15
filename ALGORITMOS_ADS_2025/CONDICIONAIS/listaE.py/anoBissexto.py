from utils import entradaInt

def ehBissexto(ano):
    return (ano % 4 == 0 and not ano % 100 == 0) or (ano % 400 == 0)


def main():
    ano = entradaInt('Insira o ano que deseja analisar: ')
    if ehBissexto(ano):
        result = 'é bissexto'
    else:
        result = 'não é bissexto'

    print(f'O ano {ano} {result}')   


main()