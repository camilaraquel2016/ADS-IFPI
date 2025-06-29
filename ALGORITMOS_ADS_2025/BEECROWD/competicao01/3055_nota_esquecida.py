def obter_nota_esquecida(nota1, media):
    return media * 2 - nota1


def main():
    nota1 = int(input())
    media = int(input())
    nota_esquecida = obter_nota_esquecida(nota1, media)
    print(nota_esquecida)

main()    