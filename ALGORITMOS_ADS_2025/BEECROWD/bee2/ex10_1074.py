def eh_par(num):
    return num % 2 == 0


def eh_positivo(num):
    return num > 0


def saida(numero):
    if numero == 0:
        return 'NULL'
    
    else:
        resposta1 = 'EVEN' if eh_par(numero) else 'ODD'
        resposta2 = 'POSITIVE' if eh_positivo(numero) else 'NEGATIVE'
        return f'{resposta1} {resposta2}'


def obter_resultados(qtd_analise):
    for analise in range(qtd_analise):
        numero = int(input())
        print(saida(numero))
        

def main():
    qtd_analise = int(input())
    obter_resultados(qtd_analise)

main()    

