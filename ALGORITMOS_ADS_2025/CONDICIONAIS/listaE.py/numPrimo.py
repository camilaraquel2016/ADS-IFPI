from utils import entradaInt

def eh_primo(num):
    if num == 1: # o número 1 é primo, pois tem apenas 1 divisor e para ser primo, precisa de 2 divisores, obrigatoriamente
        return False
    else:
        return (num == 2 or num == 3 or num == 5 or num == 7) or (not num % 2 == 0 and not num % 3 == 0 and not num % 5 == 0 and not num % 7 == 0) # para um número ser primo ele não pode ser divisível por 2, 3, 5, 7 (mas caso o número seja algum desses ele é primo). 
   
    
def main():
    num = entradaInt('Qual número deseja verificar se é primo? ')

    if eh_primo(num):
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')


main()


