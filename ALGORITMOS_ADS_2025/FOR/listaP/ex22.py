def obter_resultados(qtd_fichas):
    final = qtd_fichas + 1
    maior_peso = 0
    menor_peso = float('inf')
    
    
    for peso in range(1, final, 1):

        print('-=' * 10)
        num_identificacao = int(input('N° de identificação: '))
        nome_boi = str(input('Nome do boi: '))
        peso_do_boi = float(input('Peso do boi: (Kg) '))
        

        if peso_do_boi > maior_peso:
            maior_peso = peso_do_boi
            identificacao_maior = num_identificacao

        if peso_do_boi < menor_peso:
            menor_peso = peso_do_boi
            identificacao_menor = num_identificacao

    return f'''
    Maior peso: {maior_peso:.1f} --> N° de indentificação: {identificacao_maior}
    Menor peso: {menor_peso:.1f} --> N° de indentificação: {identificacao_menor}'''
           
        
def main():
    qtd_fichas = int(input('Quantidade de fichas: '))
    resultado = obter_resultados(qtd_fichas)

    print(resultado)

main()    
