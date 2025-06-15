from itertools import count
from utils import obter_real_positivo, obter_num_inteiro, obter_inteiro_positivo

def obter_peso_da_carga(qtd_containers):
    somatorio_peso = 0

    for container in range(1, qtd_containers + 1, 1):
        peso = obter_real_positivo(f'Peso do {container}° container: ')

        somatorio_peso += peso

    return somatorio_peso        


def saida(qtd_passageiros, peso_total_passageiros, peso_bagagens):
    return f'''
    Quantidade de passageiros: {qtd_passageiros}
    Peso total dos passageiros: {peso_total_passageiros} Kg
    Peso total de bagagens: {peso_bagagens} Kg
    '''


def obter_peso_passageiro(peso_por_passageiro, peso_por_bagagem):
    somatorio_passageiro = 0
    somatorio_bagagem = 0

    for passageiro in count():
        num_bilhete = obter_num_inteiro('N° do bilhete: (flag = 0) ')
        
        if num_bilhete == 0:
            print(saida(passageiro, somatorio_passageiro, somatorio_bagagem))
            return somatorio_passageiro + somatorio_bagagem
        
        qtd_bagagem = obter_inteiro_positivo('Quantidade de bagagens: ')

        somatorio_passageiro += peso_por_passageiro
        somatorio_bagagem += (peso_por_bagagem * qtd_bagagem)


def calcular_combustivel_possivel(peso_de_decolagem, peso_passageiro, peso_da_carga): # retorna em litro
    peso_passageiro_e_carga = peso_passageiro + peso_da_carga

    return converter_kg_para_litro(peso_de_decolagem - peso_passageiro_e_carga)

   
def eh_possivel_levantar_voo(combustivel_possivel_litro, limite_min_combustivel_litro):
    return combustivel_possivel_litro >= limite_min_combustivel_litro
     

def converter_litro_para_kg(qtd_litros):
    return qtd_litros * 1.5


def converter_kg_para_litro(qtd_kg):
    return qtd_kg / 1.5


def main():
    limite_min_combustivel_litro = 10000
    limite_min_combustivel_kg = converter_litro_para_kg(limite_min_combustivel_litro)

    peso_de_cada_passageiro = 70
    peso_de_cada_bagagem = 10
    peso_de_decolagem = 500000
    
    qtd_container = obter_inteiro_positivo('Quantidade de container: ')
    peso_da_carga = obter_peso_da_carga(qtd_container)
    peso_total_passageiro = obter_peso_passageiro(peso_de_cada_passageiro, peso_de_cada_bagagem)

    combustivel_possivel_em_litro = calcular_combustivel_possivel(peso_de_decolagem, peso_total_passageiro, peso_da_carga) # em litro

    print(f'    Peso da carga: {peso_da_carga:.1f} Kg\n ')

    if eh_possivel_levantar_voo(combustivel_possivel_em_litro, limite_min_combustivel_litro):
        print(f'É possível levantar vôo!\nQuantidade disponível de combutível: {combustivel_possivel_em_litro:.1f} litros')
    else:
        print(f'Não é possível levantar vôo!') 

main()


    

    



    
     


