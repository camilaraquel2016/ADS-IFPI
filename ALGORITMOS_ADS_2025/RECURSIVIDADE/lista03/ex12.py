from utils import obterNumInteiro

def calcularValores(qtdNum, contador = 1, soma = 0):
    if contador > qtdNum:
        return f'Soma: {soma}\nMédia: {soma / qtdNum}'
    
    num = obterNumInteiro(f'{contador}° número: ')
    contador += 1
    soma += num
    
    return calcularValores(qtdNum, contador, soma)


def main():
    qtdValores = obterNumInteiro('Quantidade de valores: ')
    resultado = calcularValores(qtdValores, 1)
    print(resultado)

main()    


