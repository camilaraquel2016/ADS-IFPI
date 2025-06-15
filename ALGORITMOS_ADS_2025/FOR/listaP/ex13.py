def obter_maior(qtd_valores):
    maior = 0
    qtd_valores += 1

    for i in range(1, qtd_valores, 1):
        num = int(input(f'{i}° número:  '))
        if num > maior:
            maior = num

    return maior 


def main():
    qtd_valores = int(input('Quantidade de valores: '))
    maior = obter_maior(qtd_valores)

    print(f'Dentre os números inseridos o maior é o {maior}')

main()





