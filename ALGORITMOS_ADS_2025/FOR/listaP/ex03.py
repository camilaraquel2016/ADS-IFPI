#O ÚLTIMO TERMO NÃO FAZ PARTE DA PA, POIS A QUESTÃO PEDE PARA ESCREVER OS TERMOS MENORES QUE O LIMITE FINAL

def exibirPA(limite_inicial, limite_final, razao):
    for i in range(limite_inicial, limite_final, razao):
        print(i)


def main():
    limite_inicial = int(input('Limite inicial: '))
    limite_final = int(input('Limite final: '))
    razao = int(input('Razão: '))

    print(F'-=-PA DE {limite_inicial} A {limite_final} COM RAZÃO {razao}-=-')
    exibirPA(limite_inicial, limite_final, razao)

main()    

