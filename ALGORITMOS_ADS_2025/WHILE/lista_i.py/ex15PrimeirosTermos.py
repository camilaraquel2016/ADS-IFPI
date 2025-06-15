from utils import obterNumInt

def listarTermos(numInicial, qtdNum):
    contador = 1
    aumento = 2

    while contador <= qtdNum:
        print(numInicial, end = '')
        numInicial += aumento
        aumento += 1
        contador += 1
        if contador <= qtdNum:
            print(', ', end = '') 

def main():
    numIncial = obterNumInt('Número inicial da sequência: ')
    qtdTermos = obterNumInt('Quantidade de termos da sequência: ')

    print(f'-=-Sequência de {qtdTermos} termos-=-')
    listarTermos(numIncial, qtdTermos)

main()    
