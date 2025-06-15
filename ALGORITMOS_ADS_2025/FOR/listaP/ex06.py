def exibir_tabuada(num):
    for i in range(1, 11, 1):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')


def main():
    num = int(input('Deseja saber a tabuada de qual número? '))
    print(f'-=-TABUADA DE {num}-=-')
    exibir_tabuada(num)

main()    
