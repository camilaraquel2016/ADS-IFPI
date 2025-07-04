def eh_positivo(num):
    return num > 0


def obter_qtd_num_positivos(valores):
    qtd_num_positivo = 0

    for num in valores:
        if eh_positivo(num):
            qtd_num_positivo += 1

    return qtd_num_positivo  


def obter_valores():
    valores = []

    for i in range(6):
        valor = float(input())
        valores.append(valor)
    
    return valores    


def main():
    valores = obter_valores()
    qtd_num_positivos = obter_qtd_num_positivos(valores)
    print(f'{qtd_num_positivos} valores positivos')

main()    
    

