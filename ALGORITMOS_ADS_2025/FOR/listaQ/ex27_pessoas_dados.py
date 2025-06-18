from utils import obter_inteiro_no_intervalo, obter_inteiro_maior_que_0

def menu_sexo():
    print('-=-=-SEXO-=-=-\n1 - Masculino\n2 - Feminino\n')


def menu_estado_civil():
    print(f'-=-=-ESTADO CIVIL-=-=-\n1 - Casado\n2 - Solteiro\n3 - Divorciado\n4 - Viúvo')    


def exibir_saida(idade_total_mulheres, qtd_mulheres, idade_total_homens, qtd_homens, total_homens_solteiros, total_mulheres_solteiras, qtd_mulheres_divorciadas_mais_de_30):
    resposta = ''

    if qtd_mulheres > 0:
        resposta += f'''
        Média de idade das mulheres: {idade_total_mulheres / qtd_mulheres}
        Percentual de mulheres solteiras: {total_mulheres_solteiras / qtd_mulheres * 100:.1f}%
        Quantidade de mulheres divorciadas acima de 30 anos: {qtd_mulheres_divorciadas_mais_de_30}'''

    if qtd_homens > 0:
        resposta += f''' 
        Média de idade dos homens: {idade_total_homens / qtd_homens}
        Percentual de homens solteiros: {total_homens_solteiros / qtd_homens * 100:.1f}%'''    

    return resposta


def obter_resultados(qtd_pessoas):
    qtd_mulheres = 0
    qtd_homens = 0
    idade_total_mulheres = 0
    idade_total_homens = 0
    total_homens_solteiros = 0
    total_mulheres_solteiras = 0
    total_mulher_divorciada_mais_de_30_anos = 0

    for pessoa in range(1, qtd_pessoas + 1):

        print(f'-=-{pessoa}° pessoa-=-')
        print()
        menu_sexo()
        sexo = obter_inteiro_no_intervalo('>>> ', 1, 2)
        print()
        menu_estado_civil()
        estado_civil = obter_inteiro_no_intervalo('>>> ', 1, 4)
        idade = obter_inteiro_no_intervalo('Idade: ', 1, 150)
        print()

        if sexo == 1:
            qtd_homens += 1
            idade_total_homens += idade

            if estado_civil == 2:
                total_homens_solteiros += 1

        else:
            qtd_mulheres += 1
            idade_total_mulheres += idade

            if estado_civil == 2:
                total_mulheres_solteiras += 1

            elif estado_civil == 3:
                if idade > 30:
                    total_mulher_divorciada_mais_de_30_anos += 1    

    return exibir_saida(idade_total_mulheres, qtd_mulheres, idade_total_homens, qtd_homens, total_homens_solteiros, total_mulheres_solteiras, total_mulher_divorciada_mais_de_30_anos)


def main():
    qtd_pessoas = obter_inteiro_maior_que_0('Quantidade de pessoas a serem entrevistadas: ')
    resultado = obter_resultados(qtd_pessoas)
    print(resultado)

main()    

