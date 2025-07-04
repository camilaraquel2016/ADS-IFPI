def possui_tres_duplas_consecutivas(palavra):
    contador_verdadeiro = 0
    contador_falso = 0
    auxiliar = ""

    for i in palavra:
        if i == auxiliar:
            contador_verdadeiro+=1
            contador_falso = 0
        else:
            contador_falso+=1

        if contador_falso == 2 :
            contador_verdadeiro = 0
            contador_falso = 0

        if contador_verdadeiro == 3:
            break
        auxiliar = i

    return contador_verdadeiro



def main():
    palavra = input("INFORME UMA PALAVRA: ")
    resultado = possui_tres_duplas_consecutivas(palavra)
    if resultado == 3:
        print('PASSOU')
    else:
        print("REPROVADO")
    pass


main()
    