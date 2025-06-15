from random import randint

def advinhacao(num_sorteado, qtd_chances):
    for tentativa in range(1, qtd_chances + 1, 1):

        num_da_vez = int(input(f'{tentativa}° tentativa: '))
        

        if num_sorteado > num_da_vez:
            print('É MAIOR')
            continue

        if num_sorteado < num_da_vez:
            print('É MENOR')
            continue

        return f'Você acertou!'

    return f'Chances esgostadas!...\nVocê perdeu'

    
def main():
    qtd_chances = 5
    num_sorteado = randint(1, 50)  
    print(advinhacao(num_sorteado, qtd_chances))
  
main()    



            


    
            
