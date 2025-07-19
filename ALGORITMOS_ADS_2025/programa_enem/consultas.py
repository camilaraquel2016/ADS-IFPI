from utils import *
from time import sleep


def exibir_top_n_todas_as_areas(lista_de_escolas: list, qtd_de_escolas: int):
    n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, qtd_de_escolas)
    lista_ordenada = ordenar_por_todas_as_areas(lista_de_escolas)
    posicao = 1
    
    print(f'-=-=-=-=-=-=-=-=-TOP {n} ESCOLAS (TODAS AS ÁREAS)-=-=-=-=-=-=-=-')

    for escola in lista_ordenada[:n]:
        print(descricao_escola_geral(escola, posicao))
        posicao += 1
  
        
def exibir_top_n_por_area(lista_de_escolas: list, qtd_de_escolas: int):
    area = obter_area(menu_areas())
    n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, qtd_de_escolas)
    lista_ordenada = ordenar_por_area(lista_de_escolas, area)
    posicao = 1

    print(f'-=-=-=-=-=-=-=-=-TOP {n} ESCOLAS ({area.upper()})-=-=-=-=-=-=-=-')

    for escola in lista_ordenada[:n]:
        print(descricao_escola_por_area(escola, posicao, area))
        posicao += 1


def exibir_top_n_por_estado(lista_de_escolas: list):
    estado = obter_estado(menu_estados())
    escolas_desse_estado = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado)
    lista_ordenada = ordenar_por_todas_as_areas(escolas_desse_estado)
    n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_desse_estado))
    posicao = 1

    print(f'-=-=-=-=-=-=-=-=-TOP {n} ESCOLAS ({estado})-=-=-=-=-=-=-=-')

    for escola in lista_ordenada[:n]:
        print(descricao_escola_geral(escola, posicao))
        posicao += 1 


def exibir_top_n_por_estado_e_rede(lista_de_escolas: list):
    estado = obter_estado(menu_estados())
    print(f' \nEstado ({estado}) selecionado!\nSelecione agora a rede')
    enter_e_limpar()
    rede = obter_rede(obter_num_inteiro_na_faixa(menu_redes(), 1, 4))

    escolas_desse_estado_e_rede = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado and escola['rede'] == rede)
    limpar_tela()

    if len(escolas_desse_estado_e_rede) == 0:
        print(f'Esse estado não possui nenhuma escola da rede {rede}!')
        return 
        
    lista_ordenada = ordenar_por_todas_as_areas(escolas_desse_estado_e_rede)
    n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_desse_estado_e_rede))
    posicao = 1

    print(f'-=-=-=-=-=-=-=-=-TOP {n} ESCOLAS DO {estado} da rede {rede}-=-=-=-=-=-=-=-')

    for escola in lista_ordenada[:n]:
        print(descricao_escola_geral(escola, posicao))
        posicao += 1


def exibir_top_n_por_cidade(lista_de_escolas: list):
    cidades = carregar_cidades(r'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\programa_enem\cidades.txt')
    limpar_tela()

    while True:
        cidade = input('Insira o nome da cidade: (sem acentos, se houver) ').upper()

        if not esta_na_lista(cidade, cidades):
            print(' \nCidade inválida!\nEssa cidade não existe ou não está presente no ENEM de 2014')
            enter_e_limpar()

        else:
            escolas_dessa_cidade = filtrar(lista_de_escolas, lambda escola: escola['municipio'] == cidade)
            lista_ordenada = ordenar_por_todas_as_areas(escolas_dessa_cidade)
            n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_dessa_cidade))
            posicao = 1

            print(f'-=-=-=-=-=-=-=-=-TOP {n} ESCOLAS DE {cidade}-=-=-=-=-=-=-=-')

            for escola in lista_ordenada[:n]:
                print(descricao_escola_geral(escola, posicao))
                posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            break 


def exibir_media_nacional_por_area(lista_de_escolas: list):
    while True:
        area = obter_area(menu_areas())
        media = reduzir(lista_de_escolas, lambda acumulado, item: acumulado + item[f'nota_{area}'], 0) / len(lista_de_escolas) 
        limpar_tela()
        print(f'Média nacional de {formatar_area(area)}: {media:.1f}')

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            break 



def exibir_melhor_escola_por_area_e_estado(lista_de_escolas: list):
    while True:
        estado = obter_estado(menu_estados())
        limpar_tela()
        print(f'Estado ({estado}) selecionado com sucesso!\n \nInsira agora a área')
        area = obter_area(menu_areas())

        escolas_desse_estado = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado)
        melhor_escola = ordenar_por_area(escolas_desse_estado, area)[0]
        limpar_tela()

        print(f'-=-=-=-=-=-MELHOR ESCOLA DO ({estado}) NA ÁREA DE {formatar_area(area).upper()}-=-=-=-=-=-')
        print(descricao_escola_por_area(melhor_escola, 1, area))

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break 

        
def exibir_top_n_por_regiao(lista_de_escolas: list):
    regioes_com_estados = obter_regioes_com_estados()

    while True:
        regiao = obter_regiao(menu_regioes())
        limpar_tela()
        print(f'Região {regiao} selecionada com sucesso!')
        escolas_dessa_regiao = filtrar(lista_de_escolas, lambda escola: esta_na_lista(escola['estado'], regioes_com_estados[regiao]))
        n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_dessa_regiao))
        lista_ordenada = ordenar_por_todas_as_areas(escolas_dessa_regiao)
        limpar_tela()
        posicao = 1
        
        print(f'-=-=--=-=-=-=-=-TOP {n} ESCOLAS DA REGIÃO {regiao}-=-=-=-=-=-=-=-=-')

        for escola in lista_ordenada[:n]:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break     


def exibir_top_n_por_regiao_e_rede(lista_de_escolas: list):
    regioes_com_estados = obter_regioes_com_estados()

    while True:
        regiao = obter_regiao(menu_regioes())
        limpar_tela()
        print(f'Região {regiao} selecionada com sucesso!\nInsira agora a rede')
        rede = obter_rede(menu_redes())
        limpar_tela()
        print(f'Rede {rede} selecionada com sucesso!')
        escolas_dessa_regiao_e_rede = filtrar(lista_de_escolas, lambda escola: esta_na_lista(escola['estado'], regioes_com_estados[regiao]) and escola['rede'] == rede)
        lista_ordenada = ordenar_por_todas_as_areas(escolas_dessa_regiao_e_rede)
        n = obter_num_inteiro_na_faixa(' \nAgora insira o valor de N: ', 1, len(escolas_dessa_regiao_e_rede))
        limpar_tela()
        posicao = 1

        print(f'-=-=-=-=-TOP {n} ESCOLAS DA REGIÃO {regiao} DA REDE {rede.upper()}-=-=-=-=-')

        for escola in lista_ordenada[:n]:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break     
    

def exibir_top_n_por_regiao_e_area(lista_de_escolas: list):
    regioes_com_estados = obter_regioes_com_estados()

    while True:
        regiao = obter_regiao(menu_regioes())
        limpar_tela()
        print(f'Região {regiao} selecionada com sucesso!\n \nInsira agora a área de sua preferência')

        area = obter_area(menu_areas())
        limpar_tela()
        print(f'Área de {area} selecionada com sucesso!')

        escolas_dessa_regiao = filtrar(lista_de_escolas, lambda escola: esta_na_lista(escola['estado'], regioes_com_estados[regiao]))
        lista_ordenada = ordenar_por_area(escolas_dessa_regiao, area)

        n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_dessa_regiao))
        posicao = 1
        limpar_tela()
        
        print(f'-=-=-TOP {n} ESCOLAS DA REGIÃO {regiao} ({formatar_area(area).upper()})-=-=-')

        for escola in lista_ordenada[:n]:
            print(descricao_escola_por_area(escola, posicao, area))
            posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break   


def exibir_top_n_por_estado_e_rede(lista_de_escolas: list):
    while True:
        estado = obter_estado(menu_estados())
        limpar_tela()
        print(f'Estado {estado} selecionado com sucesso!\n \nInsira agora a rede')
        rede = obter_rede(menu_redes())
        limpar_tela()
        print(f'Rede {rede.upper()} selecionada com sucesso!')
    
        escolas_desse_estado_e_rede = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado and escola['rede'] == rede)
        lista_ordenada = ordenar_por_todas_as_areas(escolas_desse_estado_e_rede)

        n = obter_num_inteiro_na_faixa(' \nInsira o valor de N: ', 1, len(escolas_desse_estado_e_rede))
        limpar_tela()
        posicao = 1

        print(f'-=-=-TOP {n} ESCOLAS DO {estado} DA REDE {rede.upper()}-=-=-')

        for escola in lista_ordenada[:n]:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break
           

def exibir_top_n_por_estado_e_area(lista_de_escolas: list):
    while True:
        estado = obter_estado(menu_estados())
        limpar_tela()
        print(f'Estado {estado} selecionado com sucesso!\n \nInsira agora a área de sua preferência')
        area = obter_area(menu_areas())

        escolas_desse_estado = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado)
        lista_ordenada = ordenar_por_area(escolas_desse_estado, area)
        limpar_tela()

        n = obter_num_inteiro_na_faixa('Insira o valor de N: ', 1, len(escolas_desse_estado))
        posicao = 1
        limpar_tela()

        print(f'-=-=-TOP {n} ESCOLAS DO {estado} ({formatar_area(area).upper()})-=-=-')

        for escola in lista_ordenada[:n]:
            print(descricao_escola_por_area(escola, posicao, area))
            posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break
                  

def listar_informacoes_de_uma_escola(lista_de_escolas: list):
    while True:
        nome_da_escola = obter_nome_escola('Insira o nome da escola que deseja consultar: ')
        posicao = 1

        for escola in lista_de_escolas:
            if nome_da_escola == escola['nome']:
                print(descricao_escola_geral(escola, posicao))
                posicao += 1

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break         


def listar_todas_as_escolas_de_um_estado(lista_de_escolas: list):
    while True:
        estado = obter_estado(menu_estados())
        escolas_desse_estado = filtrar(lista_de_escolas, lambda escola: escola['estado'] == estado)
        lista_ordenada = ordenar_por_todas_as_areas(escolas_desse_estado)
        posicao = 1
        limpar_tela()

        print(f'-=-=-=-=-=-=-=-ESCOLAS DO {estado}-=-=-=-=-=-=-=-')

        for escola in lista_ordenada:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1
            resposta = obter_opcao_continuar(' \nDeseja mostrar a próxima escola desse estado? (S/N) ')
            limpar_tela()

            if resposta == 'N':
                break

        limpar_tela()    

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break        
        

def listar_todas_as_escolas_da_rede_privada(lista_de_escolas: list):
    while True:
        rede = 'Privada'
        escolas_dessa_rede = filtrar(lista_de_escolas, lambda escola: escola['rede'] == rede)
        lista_ordenada = ordenar_por_todas_as_areas(escolas_dessa_rede)
        posicao = 1
        limpar_tela()

        print(f'-=-=-=-=-=-=-=-ESCOLAS DA REDE PRIVADA-=-=-=-=-=-=-=-')

        for escola in lista_ordenada:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1
            resposta = obter_opcao_continuar(' \nDeseja mostrar a próxima escola da rede privada? (S/N) ')
            limpar_tela()

            if resposta == 'N':
                break

        limpar_tela()    

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break        
        
               

def listar_todas_as_escolas_da_rede_publica(lista_de_escolas: list):
    while True:
        redes = ['Estadual', 'Federal', 'Municipal']
        escolas_dessa_rede = filtrar(lista_de_escolas, lambda escola: esta_na_lista(escola['rede'], redes))
        lista_ordenada = ordenar_por_todas_as_areas(escolas_dessa_rede)
        posicao = 1
        limpar_tela()

        print(f'-=-=-=-=-=-=-=-ESCOLAS DA REDE PÚBLICA-=-=-=-=-=-=-=-')

        for escola in lista_ordenada:
            print(descricao_escola_geral(escola, posicao))
            posicao += 1
            resposta = obter_opcao_continuar(' \nDeseja mostrar a próxima escola da rede pública? (S/N) ')
            limpar_tela()

            if resposta == 'N':
                break

        limpar_tela()    

        continuar = obter_opcao_continuar(' \nDeseja continuar fazendo essa consulta? (S/N) ')   
        limpar_tela()    

        if continuar == 'N':
            print('Encerrando essa consulta...')
            sleep(1)
            limpar_tela()
            break        
        
        

            
        






        
        


        
        
    
    

    

     

