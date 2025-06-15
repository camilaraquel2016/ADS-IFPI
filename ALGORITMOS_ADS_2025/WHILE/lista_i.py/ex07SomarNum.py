from utils import obterNumInt

def somarNumIntervalo(limiteSuperior):
    num = 1 # estado anterior 
    somatorio = 0

    while num <= limiteSuperior: # condição de continuidade
        somatorio += num # trabalho
        num += 1 # convergência dos dados
    return somatorio   


def main():
    num = obterNumInt('Limite superior do intervalo: ')
    print(f'-=-SOMATÓRIO DE 1 ATÉ {num}-=-')
    somatorio = somarNumIntervalo(num)
    print(f'--> {somatorio}')

main()