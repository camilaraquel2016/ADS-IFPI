from utils import obter_inteiro_maior_que_0

def exibir_divisoes(x, n):
    if n > 2:
        resultado = x / n
        print(f'--> {x} / {n} = {resultado:.1f}')
        x = resultado
        n -= 1
        return exibir_divisoes(x, n)
    
    return


def main():
    x = obter_inteiro_maior_que_0('X: ')
    n = obter_inteiro_maior_que_0('N: ')
    exibir_divisoes(x, n)

main()    
