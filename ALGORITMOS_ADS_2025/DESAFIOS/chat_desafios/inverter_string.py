def inverter_string(palavra):
    palavra_invertida = ''
    for caractere in palavra:
        palavra_invertida = caractere + palavra_invertida

    return palavra_invertida


def main():
    palavra = str(input('Palavra: '))
    palavra_invertida = inverter_string(palavra)
    print(f'Palavra invertida: {palavra_invertida}')

main()


