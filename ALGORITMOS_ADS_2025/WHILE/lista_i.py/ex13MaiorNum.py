from utils import obterNumInt, validarLimiteMin

def encontrarMaior(qtdElementos: int):
    contador = 1
    maior = 0

    while contador <= qtdElementos:
        num = obterNumInt(f'{contador}° número: ')
        if num > maior:
            maior = num
        contador += 1
    return maior    


def main():
    print('-=-ENCONTRANDO O MAIOR NÚMERO-=-')
    label = 'Quantidade de números que deseja analisar: '
    qtdElementos = obterNumInt(label)
    qtdElementos = validarLimiteMin(qtdElementos, 1, label)
    
    maior = encontrarMaior(qtdElementos)
    print(f'O maior dentre os números apresentados é o {maior}')

main()


         
