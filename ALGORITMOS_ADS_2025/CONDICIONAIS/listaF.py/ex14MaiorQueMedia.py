from utils import entradaInt

def calcularMedia5Valores(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def maioresQueAMedia(n1, n2, n3, n4, n5, media):
    maiores = []

    if n1 > media:
        maiores.append(n1)
    if n2 > media:
        maiores.append(n2)
    if n3 > media:
        maiores.append(n3)
    if n4 > media:
        maiores.append(n4)
    if n5 > media:
        maiores.append(n5)
    
    if len(maiores) == 0:
        return 'NENHUM'
    else:
        return maiores
    
def main():
    n1 = entradaInt('Primeiro número: ')
    n2 = entradaInt('Segundo número: ')
    n3 = entradaInt('Terceiro número: ')
    n4 = entradaInt('Quarto número: ')
    n5 = entradaInt('Quinto número: ')

    media = calcularMedia5Valores(n1, n2, n3, n4, n5)
    maiores = maioresQueAMedia(n1, n2, n3, n4, n5, media)

    print(f'Média: {media:.2f}\nMaiores que a média: {maiores}')


main()




