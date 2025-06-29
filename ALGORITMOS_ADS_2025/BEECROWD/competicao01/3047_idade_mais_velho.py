def obter_idade_do_filho_3(idade_mae, idade_filho_1, idade_filho_2):
    return idade_mae - (idade_filho_1 + idade_filho_2)


def obter_maior(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    return maior    


def main():
    m = int(input())
    a = int(input())
    b = int(input())
    c = obter_idade_do_filho_3(m, a, b)
    idade_mais_velho = obter_maior(a, b, c)
    print(idade_mais_velho)

main()            
