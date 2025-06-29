def obter_destino(ddd):
    match ddd:
        case 61:
            return 'Brasilia'
        case 71:
            return 'Salvador'
        case 11:
            return 'Sao Paulo'
        case 21:
            return 'Rio de Janeiro'
        case 32:
            return 'Juiz de Fora'
        case 19:
            return 'Campinas'
        case 27:
            return 'Vitoria'
        case 31:
            return 'Belo Horizonte'
        case _:
            return 'DDD nao cadastrado'
        

def main():
    ddd = int(input()) 

    destino = obter_destino(ddd)
    print(destino)

main()