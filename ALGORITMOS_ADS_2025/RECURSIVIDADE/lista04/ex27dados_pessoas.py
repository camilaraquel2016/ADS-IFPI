from utils import obterNumInteiro, obter_inteiro_maior_que_0

def menu_sexo():
    return f'''
    1 - Masculino
    2 - Feminino
                '''


def menu_estado_civil():
    return f'''
    1 - Casado
    2 - Solteiro
    3 - Divorciado
    4 - Viúvo
              '''


def obter_estado_civil(label):
    estado_civil = obterNumInteiro(label)

    if estado_civil == 1 or estado_civil == 2 or estado_civil == 3 or estado_civil == 4:
        return estado_civil
    
    print('Estado civil inválido!\nInsira novamente...')
    return obter_estado_civil(label) 


def obter_sexo(label):
    sexo = obterNumInteiro(label)

    if sexo == 1 or sexo == 2:
        return sexo
    
    print('Sexo inválido!\nInsira novamente...')
    return obter_sexo(label)


def saida(total_idade_mulheres, total_idade_homens, qtd_homens_solteiros, qtd_mulheres_solteiras, qtd_mulheres_divorciadas_mais_de_30, qtd_mulheres, qtd_homens):
    if qtd_mulheres > 0:
        resposta_mulher = f'''
    Média de idade das mulheres: {total_idade_mulheres / qtd_mulheres}
    Percentual de mulheres solteiras: {qtd_mulheres_solteiras / qtd_mulheres * 100:.1f}%
    Quantidade de mulheres divorciadas acima de 30 anos: {qtd_mulheres_divorciadas_mais_de_30}'''

    else:
        resposta_mulher = '    Nenhuma mulher cadastrada'    
        
    if qtd_homens > 0:
        resposta_homem = f'''
    Média de idade dos homens: {total_idade_homens / qtd_homens}
    Percentual de homens solteiros: {qtd_homens_solteiros / qtd_homens * 100:.1f}%'''
        
    else:
        resposta_homem = '    Nenhum homem cadastrado'    
        
    return f'{resposta_mulher} {resposta_homem}'    

     
def obter_dados(qtd_pessoas, contador = 1, total_idade_mulheres = 0, total_idade_homens = 0, qtd_homens_solteiros = 0, qtd_mulheres_solteiras = 0, qtd_mulheres_divorciadas_mais_de_30 = 0, qtd_mulheres = 0, qtd_homens = 0):
    print(f'-=-{contador}° pessoa-=-')
    print(menu_sexo())
    sexo = obter_sexo('Insira o sexo: ')
    idade = obter_inteiro_maior_que_0('Idade: ')
    print(menu_estado_civil())
    estado_civil = obter_estado_civil('Insira o estado civil: ')

    if sexo == 1:
        total_idade_homens += idade
        qtd_homens += 1

        if estado_civil == 2:
            qtd_homens_solteiros += 1

    else:
        total_idade_mulheres += idade   
        qtd_mulheres += 1

        if estado_civil == 2:
            qtd_mulheres_solteiras += 1

        elif estado_civil == 3:
            if idade > 30:
                qtd_mulheres_divorciadas_mais_de_30 += 1

    if contador < qtd_pessoas:  
        return obter_dados(qtd_pessoas, contador + 1, total_idade_mulheres, total_idade_homens, qtd_homens_solteiros, qtd_mulheres_solteiras, qtd_mulheres_divorciadas_mais_de_30, qtd_mulheres, qtd_homens)
    else:
        return saida(total_idade_mulheres, total_idade_homens, qtd_homens_solteiros, qtd_mulheres_solteiras, qtd_mulheres_divorciadas_mais_de_30, qtd_mulheres, qtd_homens)         



def main():
    qtd_pessoas = 100
    print(obter_dados(qtd_pessoas, 1, 0, 0, 0, 0, 0))

main()