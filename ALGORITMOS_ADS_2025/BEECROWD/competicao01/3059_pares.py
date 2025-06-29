def somar(num1, num2):
    return num1 + num2


def estar_no_intervalo(limite_min, limite_max, num):
    return num >= limite_min and num <= limite_max


def obter_qtd_pares(tamanho_vetor, valor_min, valor_max, vetor):
    qtd_pares = 0
    index_inicio = 1

    for numero_base in vetor:

        for i in range(index_inicio, tamanho_vetor):
            num_especifico = vetor[i]
            soma = somar(numero_base, num_especifico)

            if estar_no_intervalo(valor_min, valor_max, soma):  
                qtd_pares += 1
              
        index_inicio += 1   

    return qtd_pares         


def obter_valores():
    valores = input().split()
    valores_inteiros = []

    for valor in valores:
        valores_inteiros.append(int(valor))

    return valores_inteiros    


def main():
    tamanho_vetor, i, f = obter_valores()
    vetor = obter_valores()
    qtd_pares = obter_qtd_pares(tamanho_vetor, i, f, vetor)
    print(qtd_pares)
    
main()