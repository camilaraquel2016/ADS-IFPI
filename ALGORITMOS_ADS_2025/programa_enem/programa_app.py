from utils import *
from consultas import * 

def main():
    escolas = carregar_dados(r'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\programa_enem\enem2014_nota_por_escola.txt')
    qtd_de_escolas = len(escolas)

    while True:
        opcao = obter_num_inteiro_na_faixa(menu_geral(), 1, 15)
        limpar_tela()
    
        match opcao:
            case 1:
                exibir_top_n_todas_as_areas(escolas, qtd_de_escolas)
            case 2:
                exibir_top_n_por_area(escolas)
            case 3:
                exibir_top_n_por_regiao(escolas)
            case 4:
                exibir_top_n_por_estado(escolas)
            case 5:
                exibir_top_n_por_cidade(escolas)
            case 6:
                exibir_top_n_por_regiao_e_rede(escolas)
            case 7:
                exibir_top_n_por_regiao_e_area(escolas)
            case 8:
                exibir_top_n_por_estado_e_rede(escolas)
            case 9:
                exibir_top_n_por_estado_e_area(escolas)
            case 10:
                exibir_melhor_escola_por_area_e_estado(escolas)
            case 11:
                listar_informacoes_de_uma_escola(escolas)
            case 12:
                listar_todas_as_escolas_de_um_estado(escolas)
            case 13:
                listar_todas_as_escolas_da_rede_privada(escolas)
            case 14:
                listar_todas_as_escolas_da_rede_publica(escolas)
            case 15:
                print('Encerando programa...')
                break

        enter_e_limpar()    


main()    
