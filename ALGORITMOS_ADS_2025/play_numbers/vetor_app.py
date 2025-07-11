from utils import *
from vetor_utils import *
from vetor_funcionalidades import * 

def menu_geral():
    return f'''
|>>>>>>>>>>>>>>>>>>>>> 🎮 Play Numbers 🎮 <<<<<<<<<<<<<<<<<<<<<|

        1 - Exibir todos os valores
        2 - Resetar vetor
        3 - Exibir quantidade de itens no vetor
        4 - Exibir maior e menor valor e suas posições
        5 - Exibir somatório dos valores
        6 - Exibir média dos valores
        7 - Exibir valores positivos e suas quantidades
        8 - Exibir valores negativos e suas quantidades
        9 - Atualizar todos os valores por uma regra
        10 - Adicionar novos valores
        11 - Remover itens por valor exato
        12 - Remover itens por posição
        13 - Editar valor específico por posição
        14 - Sair
    
        >>> '''


def main():
    boas_vindas()
    nome = input('Qual o seu nome? ')
    limpar_tela()
    print(f'Prazer em ter você aqui, {nome}')
    print(' \nAntes de executar o programa, preciso saber quais serão os valores usados para manipulação.\nPor favor, Analise o menu abaixo e escolha a melhor opção')
    input(' \nEnter para continuar...')
    limpar_tela()
    vetor, nome_do_arquivo = inicializar_vetor_numerico()
    limpar_tela()
    print('Inicializando vetor numérico...')
    sleep(1)
    limpar_tela()

    while True:
        opcao = obter_opcao(menu_geral(), 1, 14)
        limpar_tela()
        
        match opcao:     
            case 1:
                exibir_todos_os_valores(vetor)
            case 2:
                vetor = resetar_vetor(vetor)
            case 3:
                exibir_qtd_itens(vetor)
            case 4:
                exibir_maior_e_menor_valor_e_sua_posicao(vetor)
            case 5:
                exibir_somatorio_dos_valores(vetor)    
            case 6:
                exibir_media_dos_valores(vetor)
            case 7:
                exibir_valores_positivos_e_suas_qtds(vetor)
            case 8:
                exibir_valores_negativos_e_suas_qtds(vetor)
            case 9:
                vetor = atualizar_todos_os_valores_por_uma_regra(vetor)
            case 10:
                adicionar_novos_valores(vetor)
            case 11:
                remover_itens_por_valores(vetor)
            case 12:
                remover_itens_por_posicao(vetor)
            case 13:
                editar_valor_especifico_por_posicao(vetor)
            case 14:
                caminho_para_salvar = obter_caminho_do_arquivo(nome_do_arquivo)
                salvar_vetor_no_arquivo(vetor, caminho_para_salvar) 
                print(f'Programa encerrado com sucesso!\nFoi um prazer ter você aqui, {nome}')
                break
            case _:
                print('Opção inválida')

        input(' \nEnter para continuar...')
        limpar_tela()    
    
main()    