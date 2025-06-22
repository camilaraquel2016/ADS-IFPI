from utils import obterNumInteiro

def menu():
    return f'''
    1 - Ótimo
    2 - Bom
    3 - Regular
    4 - Péssimo'''


def obter_opiniao(label):
    opiniao = obterNumInteiro(label)

    if opiniao == 1 or opiniao == 2 or opiniao == 3 or opiniao == 4:
        return opiniao
    
    print('Opinião inválida!\nInsira novamente...')
    return obter_opiniao(label)


def obter_idade(label):
    idade = obterNumInteiro(label)

    if (idade >= 1 and idade <= 100) or idade == -1:
        return idade
    
    print('Idade inválida!\nInsira novamente...')
    return obter_idade(label)


def saida(qtd_pessoas, total_otimo, total_idade_otimo, total_regular, total_bom):
    if qtd_pessoas == 0:
        return 'Nenhuma pessoa respondeu a pesquisa!'
    
    if total_otimo > 0:
        resposta = f'Média das idades das pessoas que respoderam "Ótimo": {total_idade_otimo / total_otimo}'
    else:
        resposta = 'Média das idades das pessoas que respoderam "Ótimo": Ninguém respondeu ótimo'    
    
    return f'''
    {resposta}
    Quantidade de pessoas que respoderam "Regular": {total_regular}
    Percentual de pessoas que respoderam "Bom": {total_bom / qtd_pessoas * 100:.1f}%'''
    

def obter_dados(qtd_pessoas = 0, contador = 1, total_otimo = 0, total_idade_otimo = 0, total_regular = 0, total_bom = 0):
     print(f'-=-{contador}° pessoa-=-')
     idade = obter_idade('Insira sua idade: (flag = -1) ')

     if idade == -1:
         return saida(qtd_pessoas, total_otimo, total_idade_otimo, total_regular, total_bom)
     
     print(menu())
     opiniao = obter_opiniao('Insira sua opinião: ') 
     qtd_pessoas += 1
     
     match opiniao:
         case 1:
             total_otimo += 1
             total_idade_otimo += idade
         case 2:
             total_bom += 1
         case 3:
             total_regular

     return obter_dados(qtd_pessoas, contador + 1, total_otimo, total_idade_otimo, total_regular, total_bom)
            

def main():
    print(obter_dados(0, 1, 0, 0, 0, 0))

main()    

