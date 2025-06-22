from utils import obterNumInteiroPositivo, eh_divisor

def exibir_divisores(num, candidato_divisor = 1):

    if candidato_divisor <= num:
        if eh_divisor(candidato_divisor, num):
            print(candidato_divisor)

        return exibir_divisores(num, candidato_divisor + 1)

    return   

    
def repetir():

    num = obterNumInteiroPositivo('Insira o número: (flag = 0) ')

    if num != 0:
        print(f'-=-DIVISORES DE {num}-=-')
        exibir_divisores(num, 1)
        return repetir()
    
    return


def main():
    repetir()

main()    
