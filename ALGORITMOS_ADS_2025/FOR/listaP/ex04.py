# #O ÚLTIMO TERMO NÃO FAZ PARTE DA PG, POIS A QUESTÃO PEDE PARA ESCREVER OS TERMOS MENORES QUE O LIMITE FINAL

def exibir_pg(limite_inicial, limite_final, razao):
    num = limite_inicial

    for i in range(limite_inicial, limite_final, razao):
        if num > limite_final:
            break

        print(num)
        num *= razao


def main():
    limite_inicial = int(input('Limite inicial: '))
    limite_final = int(input('Limite final: '))
    razao = int(input('Razão: '))
    exibir_pg(limite_inicial, limite_final, razao) 

main()
    



    

