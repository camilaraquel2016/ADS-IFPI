def repartir_milhas(milhas):
    milhas_auxiliar = ""
    contador_de_digitos = 0
    for i in milhas:
        milhas_auxiliar = i + milhas_auxiliar

        if len(milhas_auxiliar) == 3:
            if eh_palidro(milhas_auxiliar):
                contador_de_digitos = 3

        if len(milhas_auxiliar) == 4:
            if eh_palidro(milhas_auxiliar):
                contador_de_digitos = 4

        if len(milhas_auxiliar) == 5:
            if eh_palidro(milhas_auxiliar):
                contador_de_digitos = 5

        if len(milhas_auxiliar) == 6:
            if eh_palidro(milhas_auxiliar):
                contador_de_digitos = 6

    return contador_de_digitos

def eh_palidro(milhas):
    milhas_auxiliar = ""
    for i in reversed(milhas):
        milhas_auxiliar += i

    return milhas_auxiliar == milhas

def main():
    entrada = input("Informe um número: ")

    valor = repartir_milhas(reversed(entrada))
    valor_2 = repartir_milhas(entrada)


    if(valor or valor_2):
        print("É palindromo")
    else:
        print("Não é palindromo")

main()        