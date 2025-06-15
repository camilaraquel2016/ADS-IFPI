def analisarBoiada():
    numBoi = int(input('N° de identificação do boi: (flag = 0 ou número negativo): '))
    menorPeso = 1000
    maiorPeso = 0
    qtdBois = 0

    while numBoi >= 1:
        pesoDoBoi = float(input('Peso do boi: (Kg) '))
        if pesoDoBoi < menorPeso:
            menorPeso = pesoDoBoi
            numDoBoiMenorPeso = numBoi
        if pesoDoBoi > maiorPeso:
            maiorPeso = pesoDoBoi
            numDoBoiMaiorPeso = numBoi
        qtdBois += 1
        print(' ')
        numBoi = int(input('N° de identificação do boi: (flag = 0 ou número negativo): '))
    if qtdBois > 0:      
        print('-=' * 10)
        return f'Quantidade de bois: {qtdBois}\nBoi de maior: N°{numDoBoiMaiorPeso}\nMaior peso: {maiorPeso}\nBoi de menor peso: N°{numDoBoiMenorPeso}\nMenor peso: {menorPeso}'    
    else:
        return f'Nenhum boi foi cadastrado!'
        




def main():
    print('-=-CADASTRO DE BOIS-=-')
    print(analisarBoiada())

main()