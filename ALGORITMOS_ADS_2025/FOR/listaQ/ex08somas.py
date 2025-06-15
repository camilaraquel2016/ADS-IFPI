from itertools import count
from utils import obterNumInt, grande_espaco


def somar_e_advinhar(num): 
    num_da_vez = obterNumInt('Insira um valor: ') 

    for i in count():
        antecessor = num_da_vez 
        num_da_vez = obterNumInt('Insira um valor: ') 
        soma = antecessor +  num_da_vez

        if soma == num:
            return f'Número encontrado: {antecessor} + {num_da_vez} = {num}'
        

def main():
    num = obterNumInt('Insira um número: ')
    grande_espaco(40)
    print(somar_e_advinhar(num))

main()    

    