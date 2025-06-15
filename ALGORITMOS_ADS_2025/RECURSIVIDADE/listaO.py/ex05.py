from utils import obterNumInteiroPositivo

def obterFatorial(num, fatorial = 1):
    if num <= 1:
        return fatorial
    else:
        return obterFatorial(num - 1, fatorial * num)
    

def main():
    num = obterNumInteiroPositivo('Deseja descobrir o fatorial de qual número: ')
    fatorial = obterFatorial(num)
    print(f'Fatorial de {num} = {fatorial}')

main()    


