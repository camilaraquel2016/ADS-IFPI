from utils import entradaFloat

def arredondarNum(num):
    parteFracionaria = num % 1

    if parteFracionaria >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    

def main():
    num = entradaFloat('Digite o número que deseja arredondar: ')

    numeroArredondado = arredondarNum(num)

    print(f'O número {num} na sua forma arredondada é: {numeroArredondado}')    

   
main()

    