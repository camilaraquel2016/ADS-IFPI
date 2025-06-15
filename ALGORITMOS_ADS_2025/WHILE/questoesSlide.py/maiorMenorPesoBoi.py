from utils import obterNumReal, obterNumInt

def indenticarMaiorMenorPeso():
    numIdentificacao = -1 
    maiorPeso = 0
    numIdentificacaoMaiorPeso = 0
    menorPeso = 1000000
    numIdentificacaoMenorPeso = 0

    while numIdentificacao != 0:
        numIdentificacao = obterNumInt('N° de identificação do boi:  (flag = 0) ')
        peso = obterNumReal('Peso do boi: (Kg) ')

        if peso > maiorPeso:
            maiorPeso = peso
            numIdentificacaoMaiorPeso = numIdentificacao

        if peso < menorPeso:
            menorPeso = peso
            numIdentificacaoMenorPeso = numIdentificacao

        print(f'O boi de N° identificador {numIdentificacaoMaiorPeso} tem peso igual a {maiorPeso:.1f} Kg, sendo considerado o boi de maior peso')        
        print(f'O boi de N° identificador {numIdentificacaoMenorPeso} tem peso igual a {menorPeso:.1f} Kg, sendo considerado o boi de menor peso')    


def main():
    indenticarMaiorMenorPeso()


main()