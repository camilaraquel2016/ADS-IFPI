from utils import obterNumInt

def obterTabuada(num):
    print(f'-=-TABUADA DE {num}-=-')
    multiplicador = 1 # estado anterior

    while multiplicador <= 10: # condição de continuidade
        # trabalho
        resultado = num * multiplicador
        print(f'    {num} x {multiplicador} = {resultado}')
        multiplicador += 1 # convergência dos dados


def main():
    num = obterNumInt('Você deseja obter a tabuada de qual número? ')
    obterTabuada(num)        

main()