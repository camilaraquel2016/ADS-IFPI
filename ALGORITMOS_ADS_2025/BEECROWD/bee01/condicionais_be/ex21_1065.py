def eh_par(num):
    return num % 2 == 0


def obter_valores(qtd_valores):
    valores = []

    for i in range(qtd_valores):
        valor = int(input())
        valores.append(valor)

    return valores    


def obter_qtd_num_pares(valores):
    qtd_num_pares = 0

    for num in valores:
        if eh_par(num):
            qtd_num_pares += 1

    return qtd_num_pares        


def main():
    qtd_valores = 5
    valores = obter_valores(5)
    qtd_num_pares = obter_qtd_num_pares(valores)
    print(f'{qtd_num_pares} valores pares')
    
main()    
