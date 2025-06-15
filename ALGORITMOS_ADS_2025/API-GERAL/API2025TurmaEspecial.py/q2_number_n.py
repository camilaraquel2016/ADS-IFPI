from q1_number_utils import obterNumInt
# início 24/05 - 12:45
# fim 24/05 - 13:33


def obterSequencia():
    somaPares = 0
    somaDosNumeros = 0
    menor = 100000
    maior = 0
    qtdNumeros = 0
    contador = 1

    while True:
        label = f'Insira o {contador}° número: '
        contador += 1
        num = obterNumInt(label)

        if num == 0:
            break

        somaDosNumeros += num
        qtdNumeros += 1

        if num % 2 == 0:
            somaPares += num

        if num > maior:
            maior = num

        if num < menor:
            menor = num

    print()        

    if qtdNumeros != 0:
        media = somaDosNumeros / qtdNumeros
        return f'Soma dos pares: {somaPares}\nMédia: {media:.1f}\nMaior número: {maior}\nMenor número: {menor}'        
    else:
        return f'Nenhum número cadastrado!'


def gerenciarSequencias(num):
    contador = 1

    while contador <= num:
        print(f'-=-{contador}° sequência-=-')
        print(obterSequencia())
        print()
        contador += 1


def main():
    num = obterNumInt('Número de sequência: ') 
    gerenciarSequencias(num)

main()    








