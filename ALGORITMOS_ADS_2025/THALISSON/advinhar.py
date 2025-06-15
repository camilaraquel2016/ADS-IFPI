from random import randint

def advinhar(num_sorteado):
    num_da_vez = int(input('Seu palpite: '))

    if num_da_vez < num_sorteado:
        print('É MAIOR')
        return advinhar(num_sorteado)

    if num_da_vez > num_sorteado:
        print('É MENOR')
        return advinhar(num_sorteado)
    
    print('Você acertou!')


def main():
    num_sorteado = randint(1, 100)
    advinhar(num_sorteado)

main()    


    


       

