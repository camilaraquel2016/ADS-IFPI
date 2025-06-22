from utils import obterNumInteiroPositivo, obterNumRealPositivo

def obter_peso_dos_passageiros(peso_por_passageiro, peso_por_bagagem, peso_total_dos_passageiros = 0, peso_total_das_bagagens = 0, qtd_passageiros = 0):
    num_bilhete = obterNumInteiroPositivo('Número do bilhete: ')

    if num_bilhete == 0:
        print('-=' * 20)
        print(f'Quantidade de passageiros: {qtd_passageiros}\nPeso total dos passageiros: {peso_total_dos_passageiros}\nPeso total das bagagens: {peso_total_das_bagagens} Kg')
        return peso_total_dos_passageiros + peso_total_das_bagagens
    
    qtd_bagagens = obterNumInteiroPositivo('Quantidade de bagagens: ')

    peso_total_dos_passageiros += peso_por_passageiro
    peso_total_das_bagagens += (qtd_bagagens * peso_por_bagagem)
    qtd_passageiros += 1

    return obter_peso_dos_passageiros(peso_por_passageiro, peso_por_bagagem, peso_total_dos_passageiros, peso_total_das_bagagens, qtd_passageiros)


def obter_peso_da_carga(qtd_container, contador = 0, peso_total_container = 0):
    if contador < qtd_container:
        contador += 1
        peso_do_container = obterNumRealPositivo(f'Peso do {contador}° container: (Kg) ')
        peso_total_container += peso_do_container
        return obter_peso_da_carga(qtd_container, contador, peso_total_container)
    
    return peso_total_container


def pode_levantar_voo(qtd_disponivel_para_combustivel_em_kg, qtd_min_combustivel_em_kg):
    return qtd_disponivel_para_combustivel_em_kg >= qtd_min_combustivel_em_kg
    

def main():
    peso_de_decolagem = 500000
    qtd_min_combustivel = 10000
    qtd_min_combustivel_em_kg = qtd_min_combustivel * 1.5
    peso_por_passageiro = 70
    peso_por_bagagem = 10
    qtd_container = obterNumInteiroPositivo('Quantidade de container: ')
    peso_da_carga = obter_peso_da_carga(qtd_container, 0, 0)
    print(f'Peso total da carga: {peso_da_carga} Kg')
    print('-=' * 20)

    peso_dos_passageiros = obter_peso_dos_passageiros(peso_por_passageiro, peso_por_bagagem, 0, 0)
    qtd_disponivel_para_combustivel_em_kg = peso_de_decolagem - (peso_da_carga + peso_dos_passageiros)
    qtd_disponivel_para_combustivel_em_litros = qtd_disponivel_para_combustivel_em_kg / 1.5
    print('-=' * 20)
    print(f'Quantidade disponível de combustível: {qtd_disponivel_para_combustivel_em_kg:.1f} Kg ou {qtd_disponivel_para_combustivel_em_litros:.1f} litros')

    if pode_levantar_voo(qtd_disponivel_para_combustivel_em_kg, qtd_min_combustivel_em_kg):
        print('Pode levantar voo!')
    else:
        print('Não pode levantar voo!')    

main()


