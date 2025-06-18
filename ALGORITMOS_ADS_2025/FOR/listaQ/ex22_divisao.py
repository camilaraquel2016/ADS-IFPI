from itertools import count
from utils import obter_num_inteiro

def obter_quociente_e_resto(dividendo, divisor):
   
    for divisao in count(): 

        if dividendo < divisor:

            resto = dividendo

            return divisao, resto
        
        dividendo -= divisor 



def main():
    dividendo = obter_num_inteiro('Insira o dividendo: (número a ser dividido) ')
    divisor = obter_num_inteiro('Insira o divisor: ')

    resultado = obter_quociente_e_resto(dividendo, divisor)

    quociente = resultado[0]
    resto = resultado[1]

    print(f'{dividendo} dividido por {divisor}\nQuociente = {quociente}\nResto = {resto}')
    
main()




