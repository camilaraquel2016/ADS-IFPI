from utils import entradaInt, validarNum2Digitos, valorDezena, valorUnidade

def IgualDiferente(n1, n2):
    if n1 == n2:
        return 'iguais'
    else:
        return 'diferentes'
    

def main():
    num = entradaInt('Digite um número de 2 dígitos: ')
    num = validarNum2Digitos(num, 'Digite um número de 2 dígitos: ')

    dezena = valorDezena(num)
    unidade = valorUnidade(num)

    print(f'O número {num} tem algorismo de dezena e unidade {IgualDiferente(dezena, unidade)}')    


main()