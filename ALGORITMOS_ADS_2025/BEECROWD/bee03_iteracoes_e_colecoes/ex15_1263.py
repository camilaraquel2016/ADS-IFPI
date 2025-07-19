def obter_qtd_aliteracao(frase: str):
    contador_fixo = 0
    contador_temporario = 0

    partes = frase.split()

    palavra_antecessora = partes[0]

    for index in range(1, len(partes) + 1):
        print(f'aqui {partes[1]}')
        palavra_atual = partes[index]

        if palavra_antecessora[0] == palavra_atual[0]:
            contador_temporario += 1
        else:
            if contador_temporario > 0:
                contador_fixo += 1

            contador_temporario = 0    

        palavra_antecessora = palavra_atual

    return contador_fixo     

        


        






def main():
    frase = input().upper()
    print(obter_qtd_aliteracao(frase))

main()