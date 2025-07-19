def main():
    texto = input()
    tamanho_texto = len(texto)

    if tamanho_texto <= 140:
        print('TWEET')
    else:
        print('MUTE')

main()            
