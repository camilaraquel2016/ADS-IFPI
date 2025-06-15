def obterNumCasos(label: str):
    while True:
        numCasos = input(label).upper()

        if numCasos == 'FIM':
            return numCasos 
        
        try:
            numCasos = int(numCasos)
            if numCasos >= 0:
                return numCasos
        except ValueError:
            pass
        print('Valor não computado!')     

                   
def calcularVariacao(valorIncial: int, valorFinal: int): 
    return (valorFinal - valorIncial) / valorIncial * 100


def classificarConceito(variacao: float):
    return 'Em queda' if variacao < -15 else 'Em estabilidade' if variacao >= -15 and variacao <= 15 else 'Em alta'


def imprimirResultados(diaAtual, numCasosAnterior, totalDeCasos, qtdDias):
    while True:
        diaAtual += 1
        numCasosAtual = obterNumCasos(f'Número de casos dia {diaAtual}: (flag = "fim") ')

        if numCasosAtual != 'FIM':
            totalDeCasos += numCasosAtual
            qtdDias += 1
            variacao = calcularVariacao(numCasosAnterior, numCasosAtual)
            conceito = classificarConceito(variacao)
            print(f'Conceito do dia: "{conceito}"')
            numCasosAnterior = numCasosAtual   
        else:
            media = totalDeCasos / qtdDias
            return f'Total de casos: {totalDeCasos}\nMédia de casos por dia: {media:.1f}\nEncerrando programa...'
                
def main():
    print('-=-ANÁLISE DA EVOLUÇÃO DA COVID-=-')
    diaAtual = 1
    qtdDias = 1 
    numCasos = obterNumCasos(f'Número de casos dia {diaAtual}: (flag = "fim") ')

    if numCasos == 'FIM':
        print('encerrando programa...')
    else:
        print('Ainda não é possível exibir o conceito, pois esse é o primeiro valor registrado!')
        totalDeCasos = numCasos
        print(imprimirResultados(diaAtual, numCasos, totalDeCasos, qtdDias))
        

main()
