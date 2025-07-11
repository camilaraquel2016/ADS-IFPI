from time import sleep
from random import uniform
from utils import *
from vetor_utils import *

def inicializar_vetor_numerico():
    opcao_geral = obter_num_inteiro_na_faixa(menu_inicializar(), 1, 2)
    limpar_tela()

    if opcao_geral == 1:
        print(' \nÓtimo! Você escolheu criar os valores de forma automática\nPara isso você deve informar...')
        tamanho_do_vetor = obter_num_inteiro_com_limite_min(' \nTamanho do vetor: ', 1)
        limite_min = obter_num_real('Limite mínimo dos números: ')
        limite_max = obter_num_real_com_limite_min('Limite máximo dos números: ', limite_min + 1)
        return gerar_vetor_aleatorio(tamanho_do_vetor, limite_min, limite_max), 'vetor_principal'

    else:
        limpar_tela()
        print(' \nÓtimo! Você escolheu criar os valores de forma automática\nPara isso você deve informar se deseja...') 
        opcao_especifica = obter_num_inteiro_na_faixa(menu_gerar_manual(), 1, 2)
        limpar_tela()

        if opcao_especifica == 1:

            while True:

                opcao_arquivo = obter_num_inteiro_na_faixa(exibir_arquivos_exemplos(), 1, 5)
                nome_do_arquivo = obter_nome_do_arquivo(opcao_arquivo)
                caminho_do_arquivo = obter_caminho_do_arquivo(nome_do_arquivo)
                vetor = carregar_vetor_do_arquivo(caminho_do_arquivo)
                if len(vetor) > 0:
                    return vetor, nome_do_arquivo
                
                print(' \nEsse arquivo está vazio, logo não pode ser usado para manipulação... \nEscolha outro, por favor')
                input(' \nEnter para continuar...')
                limpar_tela()
                      
        else:
            print('Boa escolha! Criar o seu próprio vetor, com valores escolhidos por você.')
            print(f'Para isso informe...')
            tamanho_do_vetor = obter_num_inteiro_com_limite_min('Tamanho do vetor: ', 1)
            limite_min = obter_num_real('Limite mínimo dos números: ')
            limite_max = obter_num_real_com_limite_min('Limite máximo dos números: ', limite_min + 1)
            return criar_vetor_manualmente(tamanho_do_vetor, limite_min, limite_max), 'vetor_principal'

    
def exibir_todos_os_valores(vetor):
    contador = 1
    
    print(f'-=-EXIBIÇÃO DE TODOS OS VALORES-=-\n ')
    for valor in vetor:
        print(f'{10 * ' '}{contador}° valor: {valor:.2f}')
        contador += 1


def resetar_vetor(vetor):
    valor_padrao = obter_num_real('Insira o número padrão: ')
    print(f' \nProntinho, todos os {len(vetor)} valores presentes no vetor foram resetados para {valor_padrao}')
    return mapear(vetor, lambda valor: valor_padrao)


def exibir_qtd_itens(vetor):
    print(f'O vetor atual possui {len(vetor)} itens')

   
def exibir_maior_e_menor_valor_e_sua_posicao(vetor):
    index = 0
    maior = reduzir(vetor, obter_maior, vetor[0])
    menor = reduzir(vetor, obter_menor, vetor[0])

    posicoes_que_o_maior_assume = ''
    posicoes_que_o_menor_assume = ''

    for valor in vetor:
        if valor == maior:
            posicoes_que_o_maior_assume += f'{index}, '

        if valor == menor:
            posicoes_que_o_menor_assume += f'{index}, '

        index += 1    

    print(f' \nMaior valor: {maior}\nPosições que o valor {maior} assume: {posicoes_que_o_maior_assume.strip(', ')}')   
    print(f' \nMenor valor: {menor}\nPosições que o valor {menor} assume: {posicoes_que_o_menor_assume.strip(', ')}')          


def exibir_media_dos_valores(vetor):
    tamanho_do_vetor = len(vetor)

    if tamanho_do_vetor == 0:
        print(f'O vetor está vazio!')
    else:
        media = reduzir(vetor, somar, 0) / tamanho_do_vetor
        print(f'Média dos valores: {media:.1f}')


def exibir_valores_positivos_e_suas_qtds(vetor):
    valores_positivos = filtrar(vetor, eh_positivo)
    qtd_valores_positivos = len(valores_positivos)

    if qtd_valores_positivos > 0:
        print(f'-=-EXIBIÇÃO DOS VALORES POSITIVOS-=-')
        contador = 1

        for valor in valores_positivos:
            print(f'{10 * ' '}{contador}° valor: {valor}')
            contador += 1
        print(f' \nQuantidade de valores positivos: {qtd_valores_positivos}')   
    else:
        print('Nenhum valor positivo presente no vetor atual!')


def exibir_valores_negativos_e_suas_qtds(vetor):
    valores_negativos = filtrar(vetor, eh_negativo)
    qtd_valores_negativos = len(valores_negativos)

    if qtd_valores_negativos > 0:
        print(f'-=-EXIBIÇÃO DOS VALORES NEGATIVOS-=-')
        contador = 1

        for valor in valores_negativos:
            print(f'{10 * ' '}{contador}° valor: {valor}')
            contador += 1
        print(f' \nQuantidade de valores negativos: {qtd_valores_negativos}')    
    else: 
        print('Nenhum valor negativo presente no vetor atual!')       


def adicionar_novos_valores(vetor: list):
    qtd_valores_para_adicionar = obter_num_inteiro_com_limite_min('Quantos valores deseja adicionar? ', 1)
    str_de_parada = 'PARAR'

    for insercao in range(1, qtd_valores_para_adicionar + 1):
        input(' \nEnter para continuar...')
        limpar_tela() 

        valor = obter_valor_a_ser_adicionado(f'{insercao}° valor a ser adicionado: (flag = PARAR) ', str_de_parada)

        if valor == str_de_parada:
            print('Acão de ADICIONAR VALORES interrompida com sucesso!')
            break

        vetor.append(valor)
        print(f'Valor {valor} adicionado com sucesso!')

               
def remover_itens_por_valores(vetor: list):
    qtd_valores_para_remover = obter_num_inteiro_com_limite_min('Quantos valores deseja remover? ', 1)  
    str_de_parada = 'PARAR'

    for remocao in range(1, qtd_valores_para_remover + 1): 
        input(' \nEnter para continuar...')
        limpar_tela() 

        valor = obter_num_a_ser_removido(f'{remocao}° valor a ser removido: (flag = PARAR) ', vetor, str_de_parada)

        if valor == str_de_parada:
            print('Ação de REMOVER VALORES interrompida com sucesso!')
            break
        else:
            vetor.remove(valor)
            print(f'Valor {valor} removido com sucesso!')
  

def exibir_somatorio_dos_valores(vetor: list):
    somatorio = reduzir(vetor, somar, 0)
    print(f'O somatório dos valores atuais do vetor é {somatorio}')


def remover_itens_por_posicao(vetor: list):
    while True:
        if len(vetor) == 0:
            print('Não é possível mais remover itens, pois o vetor está vazio!')
            break
        
        num_da_posicao = obter_num_inteiro_com_limite_min('Insira a posição do valor que deseja remover\nLembrando que o primeiro valor começa na posição 0\n>>> ', 0)
        
        if eh_posicao_valida(num_da_posicao, vetor):
            vetor.remove(vetor[num_da_posicao])
            print('Item removido com sucesso!')
        else:
            print(f'Posição inválida!\nA maior posição que o vetor assume é a posição {len(vetor) - 1}')    
        
        input(' \nEnter para continuar...')
        limpar_tela()

        resposta = obter_resposta(' \nDeseja continuar removendo? (S/N) ', 'S', 'N')

        if resposta == 'N':
            print('Ação de REMOVER ITENS POR POSIÇÃO interrompida com sucesso!')
            break

        input(' \nEnter para continuar...')
        limpar_tela()


def editar_valor_especifico_por_posicao(vetor: list):

    while True:
        posicao = obter_num_inteiro_com_limite_min('Insira a posição que deseja editar: ', 0)

        if eh_posicao_valida(posicao, vetor):
            print(f' \nAtualmente a posição {posicao} contém o valor {vetor[posicao]}')
            novo_valor = obter_num_real(f'Qual será o novo valor dessa posição? ')
            vetor[posicao] = novo_valor
            print('Valor editado com sucesso!')
        else:
            print(f'Posição inválida!\nA maior posição que o vetor assume é a posição {len(vetor) - 1}')

        input(' \nEnter para continuar...')
        limpar_tela()    

        resposta = obter_resposta(' \nDeseja continuar editando os valores? (S/N) ', 'S', 'N')

        if resposta == 'N':
            print('Ação de EDITAR VALORES POR POSIÇÃO interrompida com sucesso!')
            break

        input(' \nEnter para continuar...')
        limpar_tela()


def atualizar_todos_os_valores_por_uma_regra(vetor: list):
    while True:
        regra = obter_opcao(menu_alterar_valores(), 0, 6)
        limpar_tela()

        match regra:
            case 0:
                print('\nSaindo da opção ATUALIZAR TODOS OS VALORES...')
                sleep(1)
                return vetor
            case 1:
                print(' \nVamos multiplicar todos os valores por um número de sua escolha...')
                multiplicador = obter_num_real('Insira o valor do multiplicador: ')
                print(f'Todos os valores foram multiplicados por {multiplicador}')
                vetor = mapear(vetor, lambda valor: valor * multiplicador)
            case 2:
                print(' \nVamos elevar todos os valores por um número de sua escolha...')
                expoente = obter_num_inteiro_na_faixa('Insira o valor do expoente: ', 0, 50) # para evitar alguns problemas, usei restrições quanto ao expoente
                print(f'Todos os valores foram elevados a {expoente}')
                vetor = mapear(vetor, lambda valor: valor ** expoente)
            case 3:
                print(' \nVamos reduzir todos os número por uma fração. Para isso informe a fração...')
                numerador = obter_num_inteiro_com_limite_min('Insira o numerador: ', 0)
                print(f'Lembrando que como é uma REDUÇÃO DE VALOR você deve inserir um valor no denominador maior que o numerador, ou seja, maior que {numerador}')
                denominador = obter_num_inteiro_com_limite_min('Insira o denominador: ', numerador + 1)
                vetor = mapear(vetor, lambda valor: numerador * valor / denominador)
            case 4:
                print(' \nVamos substituir os valores negativos por um número aleatório...\nPara isso insira os valores mínimo e máximo do número aleatório.')
                limite_min = obter_num_real('Limite mínimo: ')
                limite_max = obter_num_real_com_limite_min('Limite  máximo: ', limite_min + 1)
                numero_substituto = round(uniform(limite_min, limite_max), 2)
                print(f'Pronto! Todos os valores negativos que existiam foram substituídos pelo número aleatório {numero_substituto}')
                vetor = mapear(vetor, lambda valor: numero_substituto if eh_negativo(valor) else valor)
            case 5:
                print(' \nVamos ordenar os valores, para isso, informe se deseja ordenar de forma...')
                opcao = obter_num_inteiro_na_faixa(' \n1 - Crescente\n2 - Decrescente\n \n>>> ', 1, 2)
                valor_boo = True if opcao == 2 else False
                print(f'Prontinho, seu vetor já está em ordem {'crescente' if opcao == 1 else 'decrescente'}, assim como você pediu.')
                vetor = sorted(vetor, reverse=valor_boo)
            case 6:
                print(' \nVamos embaralhar os valores do seu vetor, para isso, preciso que você me ajude...')
                print(' \nLembrando que quanto maior a quantidade de embaralhamentos, maior a probabilidade dele ficar MUITO embaralhado...')
                qtd_embaralhamentos = obter_num_inteiro_com_limite_min(' \nDiga-me quantas vezes devo embaralhar seu vetor: ', 1)
                limpar_tela()
                print('Prontinho, seu vetor está embaralhado!')
                vetor = embaralhar_valores(vetor, qtd_embaralhamentos)

        input(' \nEnter para continuar...')
        limpar_tela()        


def salvar_vetor_no_arquivo(vetor, caminho_para_salvar):

    arquivo = open(caminho_para_salvar, 'w')

    for valor in vetor:
        arquivo.write(f'{valor:.2f}\n')
    

    


