def obter_fatorial(num):
    fatorial = 1

    for i in range(num, 0, -1):
        fatorial *= i

    return fatorial    


def main():
    num = int(input('Deseja saber o fatorial de qual número? '))
    fatorial = obter_fatorial(num)
    print(f'O fatorial de {num} é {fatorial}')

main()    
      
    