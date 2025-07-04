def obter_nota():
    while True:
        nota = float(input())
        
        if nota >= 0 and nota <= 10:
            return nota
        
        print('nota invalida')


def obter_resposta():
    while True:
        print('novo calculo (1-sim 2-nao)')
        resposta = int(input())

        if resposta == 1 or resposta == 2:
            return resposta
    


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def obter_resultados():
    while True:
        nota1 = obter_nota()
        nota2 = obter_nota()
        media = calcular_media(nota1, nota2)
        print(f'media = {media:.2f}')

        resposta = obter_resposta()

        if resposta == 2:
            break


def main():
    obter_resultados()

main()            


    
    


