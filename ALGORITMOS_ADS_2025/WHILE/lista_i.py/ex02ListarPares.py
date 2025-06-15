from utils import obterNumInt, validarLimiteMin

def listarNumPares(numFinal: int):
    num = 1 # estado anterior

    while num <= numFinal: # condição de continuidade
        # trabalho
        if num % 2 == 0:  
            print(num, end = ' ')
            
        num += 1 # convergência dos dados


def main():
    label = 'Deseja listar todos os números pares de 1 até quanto? '
    numFinal = obterNumInt(label)
    numFinal = validarLimiteMin(numFinal, 1, label)

    print(f'-=-Número pares entre 1 a {numFinal}-=-')
    listarNumPares(numFinal)

  
main()