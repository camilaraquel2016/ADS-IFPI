import copy
from utils import *

def main():
    candidatos = carregar_candidatos(r'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\programa_eleicoes\candidatos_e_votos_vereador_THE_2012 - candidatos_e_votos_vereador_THE_2012.csv')
    coligacoes = obter_coligacoes(r'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\programa_eleicoes\partidos_e_coligacoes.txt')
    qtd_vagas_disponiveis = 29

    while True:
        opcao = obter_num_inteiro_na_faixa(menu_consultas(), 1, 7)
        limpar_tela()

        match opcao:
            case 1:
                exibir_total_de_votos_validos(candidatos)
            case 2:
                exibir_quociente_eleitoral(candidatos, qtd_vagas_disponiveis)
            case 3:
                copia_coligacoes = copy.deepcopy(coligacoes)
                exibir_total_de_votos_por_coligacao(candidatos, copia_coligacoes)
            case 4:
                copia_coligacoes = copy.deepcopy(coligacoes)
                exibir_vagas_por_quociente_partidario(candidatos, qtd_vagas_disponiveis, copia_coligacoes)
            case 5:
                copia_coligacoes = copy.deepcopy(coligacoes)
                exibir_vagas_de_sobra(copia_coligacoes, candidatos, qtd_vagas_disponiveis)
            case 6:
                copia_coligacoes = copy.deepcopy(coligacoes)
                exibir_vereadores_eleitos(copia_coligacoes, candidatos, qtd_vagas_disponiveis)
            case 7:
                exibir_eleitos_sem_a_regra(candidatos, qtd_vagas_disponiveis)

        enter_e_limpar()


main()    

