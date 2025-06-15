from utils import obterNumInt, validarLimiteMin

def obterMaiorQuadrado(num):
    raizDeNum = int(num ** 0.5)
    raizAoQuadrado = raizDeNum ** 2

    while num != raizAoQuadrado: 
        num -= 1  
        raizDeNum = int(num ** 0.5)
        raizAoQuadrado = raizDeNum ** 2
        
    return num


def main():
    label = 'Insira o valor que deseja analisar: '
    num = obterNumInt(label)
    num = validarLimiteMin(num, 1, label)

    maiorQuadrado = obterMaiorQuadrado(num)

    print(f'O maior quadrado de acordo com o número inserido é {maiorQuadrado}')

main()    






    


