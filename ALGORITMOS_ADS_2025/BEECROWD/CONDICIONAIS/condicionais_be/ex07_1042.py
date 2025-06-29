def exibir_valores_ordenados(num1, num2, num3):
    if num1 > num2:
        auxiliar = num1
        num1 = num2
        num2 = auxiliar

    if num1 > num3:
        auxiliar = num1
        num1 = num3
        num3 = auxiliar

    if num2 > num3:
        auxiliar = num2
        num2 = num3
        num3 = auxiliar

    print(f'{num1}\n{num2}\n{num3}\n')


def exibir_valores(num1, num2, num3):
    print(f'{num1}\n{num2}\n{num3}')


def main():
    valores = input().split()

    num1 = int(valores[0])
    num2 = int(valores[1])
    num3 = int(valores[2])

    exibir_valores_ordenados(num1, num2, num3)  

    exibir_valores(num1, num2, num3)          

main()


        
        