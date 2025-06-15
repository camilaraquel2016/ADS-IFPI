from utils import obterNumInteiro

def exibirTabuada(num, contador = 1):
    if contador <= 10:
        resultado = num * contador
        print(f'{num} x {contador} = {resultado}')
        exibirTabuada(num, contador + 1)
         

def main():
    num = obterNumInteiro('Você deseja ver a tabuada de qual número? ')
    print(f'-=-TABUADA DE {num}-=-')
    exibirTabuada(num)

main()    