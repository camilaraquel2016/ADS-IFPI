def encontrou(palavra, texto, posicao):
    comeco, fim = posicao, posicao + len(palavra) 
    return texto[comeco: fim] == palavra


def possui_palavra(palavra, texto):
    posicao = 0

    for caractere in texto:
        if caractere == palavra[0]:
            if encontrou(palavra, texto, posicao):
                return True

        posicao += 1    

    return False    


def main():
    palavra = 'ZELDA'
    string = input().upper()
    if possui_palavra(palavra, string):
        print('Link Bolado')
    else:
        print('Link Tranquilo')

main()            

