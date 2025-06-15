from utils import obterNumInt, limparTela, validarLimiteMin

def somarEAdivinha(num):
    soma = 0
    numCanditado = obterNumInt('Vamos somar e tentar advinhar...\nNúmero: ') 
    
    while soma != num:
        print(numCanditado)
        antecessor = numCanditado
        numCanditado = obterNumInt('Vamos somar e tentar advinhar...\nNúmero: ') 
        soma = antecessor + numCanditado
    return f'Fim da lista...\n{antecessor} + {numCanditado} = {num}'


def pedirNum(limiteMin, label):
    num = obterNumInt(label)
    num = validarLimiteMin(limiteMin, num, label)
    return num

def main():
    label = 'Insira o valor que vamos tentar advinhar: '
    num = pedirNum(1, label)
    limparTela()

    print(somarEAdivinha(num))

main()    


  

