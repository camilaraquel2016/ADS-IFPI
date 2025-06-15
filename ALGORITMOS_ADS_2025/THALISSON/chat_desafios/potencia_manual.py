# 2, 6
# 4, 3



def obter_potencia(base, expoente):
    potencia = 1

    for i in range(expoente):
        potencia *= base

    return potencia    


def main():
    base = int(input('Base: '))
    expoente = int(input('Expoente: '))
    potencia = obter_potencia(base, expoente)
    print(f'{base} eleveado a {expoente} = {potencia}')

main()
