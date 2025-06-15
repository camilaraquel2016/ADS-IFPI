from utils import entradaFloat, maior3Num, menor3Num

def meio3Num(maior, menor, n1, n2, n3):
    if n1 != n2 and n1 != n3 and n2 != n3:
        if n1 != maior and n1 != menor:
            return n1
        elif n2 != maior and n2 != menor:
            return n2
        else:
            return n3
    else:
        if n1 < maior:
            meio = n1
        if n2 < maior:
            meio = n2
        if n3 < maior:
            meio = n3        
    

def TodosIguais(n1, n2, n3):
    return n1 == n2 == n3


def main():
    n1 = entradaFloat('Digite o primeiro número: ')
    n2 = entradaFloat('Digite o segundo número: ')
    n3 = entradaFloat('Digite o terceiro número: ')

    maior = maior3Num(n1, n2, n3)
    menor = menor3Num(n1, n2, n3)
    meio = meio3Num(maior, menor, n1, n2, n3)

    if TodosIguais(n1, n2, n3):
        print(f'Ordem crescente: {n1}, {n2}, {n3}')
    else:
        print(f'Ordem crescente: {menor}, {meio}, {maior}')

    
main()
