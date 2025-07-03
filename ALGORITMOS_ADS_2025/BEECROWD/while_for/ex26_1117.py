def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def obter_nota(limite_min: float, limite_max: float):
    nota = float(input())

    while nota < limite_min or nota > limite_max:
        print('nota invalida')
        nota = float(input())

    return nota    


def main():
    limite_min = 0
    limite_max = 10
    nota1 = obter_nota(limite_min, limite_max)
    nota2 = obter_nota(limite_min, limite_max)
    media = calcular_media(nota1, nota2)
    print(f'media = {media:.2f}')
    
main()    


