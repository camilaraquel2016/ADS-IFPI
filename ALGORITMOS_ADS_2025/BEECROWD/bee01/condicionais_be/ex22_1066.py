def obter_valores(qtd_valores):
    valores = []

    for i in range(qtd_valores):
        valor = int(input())
        valores.append(valor)

    return valores


def eh_par(num):
    return num % 2 == 0


def eh_positivo(num):
    return num > 0


def eh_negativo(num):
    return num < 0


def obter_quantidades(valores):
    qtd_num_pares = 0
    qtd_num_impares = 0
    qtd_num_positivos = 0
    qtd_num_negativos = 0
    
    for num in valores:
        if eh_par(num):
            qtd_num_pares += 1
        else:
            qtd_num_impares += 1

        if eh_positivo(num):
            qtd_num_positivos += 1
        if eh_negativo(num):
            qtd_num_negativos += 1

    return qtd_num_pares, qtd_num_impares, qtd_num_positivos, qtd_num_negativos                    


def main():
    qtd_valores = 5
    valores = obter_valores(qtd_valores)
    qtd_num_pares, qtd_num_impares, qtd_num_positivos, qtd_num_negativos = obter_quantidades(valores)
    print(f'{qtd_num_pares} valor(es) par(es)\n{qtd_num_impares} valor(es) impar(es)\n{qtd_num_positivos} valor(es) positivo(s)\n{qtd_num_negativos} valor(es) negativo(s)')

main()
