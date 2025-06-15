from utils import entradaFloat, maior3Num

def obterHipotenusa(lado1, lado2, lado3):
    hipotenusa = lado1
    if lado2 > hipotenusa:
        hipotenusa = lado2
    if lado3 > hipotenusa:
        hipotenusa = lado3
    return hipotenusa    


def obterCatetos(lado1, lado2, lado3):
    hipotenusa = obterHipotenusa(lado1, lado2, lado3)
    catetos = []

    if lado1 != hipotenusa:
        catetos.append(lado1)
    if lado2 != hipotenusa:
        catetos.append(lado2)
    if lado3 != hipotenusa:
        catetos.append(lado3)
    return catetos           


def main():
    lado1 = entradaFloat('Lado 1: ')
    lado2 = entradaFloat('Lado 2: ')
    lado3 = entradaFloat('Lado 3: ')

    print('-=' * 10)

    hipotenusa = obterHipotenusa(lado1, lado2, lado3)
    catetos = obterCatetos(lado1, lado2, lado3)
    
    try:
        print(f'Hipotenusa: {hipotenusa}\nCateto 1: {catetos[0]}\nCateto 2: {catetos[1]}')
    except IndexError:
        print('Essas medidas não formam um triângulo retângulo')    


main()    
      

    
    