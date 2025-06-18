# questão que pode ser feita perfeitamente usando while, entretanto como é uma prática de FOR, 
# o mesmo será usado nessa questão com o auxílio da função count do módulo itertools 

from itertools import count
from utils import obter_num_inteiro, obter_inteiro_no_intervalo

def obter_idade(label):

    for tentativa in count():
        idade = obter_num_inteiro(label)

        if (idade == -1) or (idade >= 1 and idade <= 100):
            return idade
        
        print('Idade inválida!')


def menu_opinioes():
    return f'''
    1 - ótimo
    2 - bom
    3 - regular
    4 - péssimo
'''

def obter_opiniao():
    print(menu_opinioes())

    opiniao = obter_inteiro_no_intervalo('Insira sua opção: ', 1, 4)

    return opiniao


def exibir_saida(total_idade_otimo, total_otimo, total_regular, total_bom, total_entrevistados):
    if total_entrevistados > 0:
         print(f'Percentual de pessoas que respoderam BOM entre os entrevistados: {total_bom / total_entrevistados * 100:.1f} %')
         print(f'Quantidade de pessoas que responderam REGULAR: {total_regular}')

         if total_otimo > 0:
             print(f'Média das idades das pessoas que responderam ÓTIMO: {total_idade_otimo / total_otimo}')
         else:
             print(f'Nenhuma opinião do tipo "ÓTIMO" cadastrada!')    

    else:
        print(f'Nenhuma opinião cadastrada!')         
             

def obter_resultados():
    total_entrevistados = 0
    total_otimo = 0
    total_bom = 0
    total_regular = 0
    total_idade_otimo = 0

    for pessoa in count(1):
        idade = obter_idade(f'Insira idade da pessoa {pessoa}: (flag = -1) ')
        if idade == -1:
            exibir_saida(total_idade_otimo, total_otimo, total_regular, total_bom, total_entrevistados)
            break

        opiniao = obter_opiniao()

        if opiniao == 1:
            total_otimo += 1
            total_idade_otimo += idade

        elif opiniao == 3:
            total_regular += 1

        elif opiniao == 2:
            total_bom += 1

        total_entrevistados += 1    


def main():
    print('-=-QUESTINÁRIO OPINIÃO CINEMA-=-')
    obter_resultados()

main()    
        


