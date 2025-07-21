import os
import copy

# MENU E FORMATAÇÃO E AJUSTES

def descricao_eleitos(eleito: dict, contador):
    return f'''
    -----------{contador}° VEREADOR ELEITO---------------------------
    Nome vereador: {eleito['nome']}
    Nome partido: {eleito['partido']}
    Coligação: {eleito['coligacao']}
    Total votos: {eleito['total_votos']}
    ---------------------------------------------------------
'''


def menu_consultas():
    return f'''
    1 - Exibir total de votos válidos
    2 - Exibir Quociente Eletoral (QE)
    3 - Exibir total de votos por coligação
    4 - Exibir total de vagas por (Quociente Partidário)
    5 - Exibir vagas de sobra 
    6 - Exibir vereadores eleitos 
    7 - Exibir vereados que seriam eleitos sem a regra proposta

    >> '''


def limpar_tela():
    os.system('cls')
    

def enter_e_limpar():
    input(' \nEnter para continuar...')
    limpar_tela()


def resumo(lista_de_vagas_por_media, lista_atualizada):
    index = 0
    
    print('        Partido               |              Pelo QP                 |           Pela média               |       TOTAL  ')
    print('-------------------------------------------------------------------------------------------------------------------------------')

    for coligacao in lista_de_vagas_por_media:
        nome = coligacao['nome_da_coligacao']
        pelo_qp = lista_atualizada[index]['qtd_vagas']
        pela_media = coligacao['qtd_vagas_que_recebeu']
        total = pelo_qp + pela_media
        espaco1 = obter_espaco_necessario(nome)
        espaco2 = obter_espaco_necessario(str(pelo_qp))
        espaco3 = obter_espaco_necessario(str(pela_media))
        # espaco4 = obter_espaco_necessario(str(total))
        index += 1

        print(f'Coligação {nome}{espaco1}|                  {pelo_qp}{espaco2}|                {pela_media}{espaco3}|       {total}')


def obter_espaco_necessario(elemento: str):
    return ' ' * (20 - len(elemento))


# VALIDAÇÕES


def obter_num_inteiro(label: str):
    while True:
        entrada = input(label)

        try:
            num = int(entrada)
            return num
        except ValueError:
            print(f' \nEntrada inválida!\nO valor inserido deve ser um número inteiro, entretanto você inseriu o valor "{entrada}"')
            enter_e_limpar()



def obter_num_inteiro_na_faixa(label: str, limite_min: int, limite_max: int):
    while True:
        num = obter_num_inteiro(label) 

        if num >= limite_min and num <= limite_max:
            return num
        
        print(f' \nEntrada inválida!\nO valor inserido deve estar entre {limite_min} e {limite_max}')
        enter_e_limpar()


# CRIAÇÕES DE LISTAS, DICIONÁRIOS


def carregar_candidatos(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo)
    candidatos = []

    for linha in arquivo:
        dados = linha.strip().split(',')
        
        candidato = {
            'nome': dados[0],
            'numero': dados[1],
            'partido': dados[2],
            'coligacao': dados[3],
            'total_votos': int(dados[4])
        }
        
        candidatos.append(candidato)
    
    return candidatos


def obter_coligacoes(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo)
    coligacoes = []

    for linha in arquivo:

        coligacao = {
            'coligacao': linha.strip(),
            'total_votos': 0,
            'qtd_vagas': 0,
            'votos_sobra_total': 0
        }

        coligacoes.append(coligacao)

    return coligacoes    


def obter_lista_de_vagas_por_media(coligacoes):
    lista = []

    for coligacao in coligacoes:
        item = {
            'nome_da_coligacao': coligacao['coligacao'],
                'qtd_vagas_que_recebeu': 0
                }
        
        lista.append(item)

    return lista


def lista_para_guardar_media(coligoes):
    medias = []

    for coligacao in coligoes:

        media = {
            'nome_coligacao': coligacao['coligacao'],
            'media': 0
        }

        medias.append(media)

    return medias    


# FILTRAR E REDUZIR


def filtrar(colecao, funcao_criterio):
    nova_colecao = []

    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)

    return nova_colecao        


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado


# FUNÇÕES REDUTORAS


def somar(n1, n2):
    return n1 + n2


def obter_maior(n1, n2):
    return n1 if n1 > n2 else n2


# FUNÇÕES PARA OBTER ALGO/ ATUALIZAR/ MANIPULAR


def obter_nome_da_coligacao_de_maior_media(medias: list, maior_media):
    for x in medias:
        if x['media'] == maior_media:
            return x['nome_coligacao']


def obter_qtd_votos(lista_de_candidatos):
    return reduzir(lista_de_candidatos, lambda acumulado, candidato: somar(acumulado, candidato['total_votos']), 0)


def incrementar_vaga_da_media(lista_de_vagas_por_media, nome_da_coligacao_maior_media):
    for coligacao in lista_de_vagas_por_media:
        if coligacao['nome_da_coligacao'] == nome_da_coligacao_maior_media:
            coligacao['qtd_vagas_que_recebeu'] += 1


def incrementar_vaga(lista_atualizada, nome_da_coligacao_maior_media):
    for coligacao in lista_atualizada:
        if coligacao['coligacao'] == nome_da_coligacao_maior_media:
            coligacao['qtd_vagas'] += 1
            break


def obter_quociente_eleitoral(lista_de_candidatos: list, qtd_vagas_disponiveis: int):
    qtd_votos_validos = obter_qtd_votos(lista_de_candidatos)
    return qtd_votos_validos // qtd_vagas_disponiveis 


def atualizar_qtd_votos_de_cada_coligacao(lista_de_candidatos: list, lista_de_coligacoes: list):
    for candidato in lista_de_candidatos:

        for coligacao in lista_de_coligacoes:
            if candidato['coligacao'] == coligacao['coligacao']:
                coligacao['total_votos'] += candidato['total_votos']
                break

    return lista_de_coligacoes        
    

def atualizar_qtd_vagas_de_cada_coligacao(lista_de_coligacoes: list, lista_de_candidatos:  list, qtd_vagas_disponiveis: int):
    lista_de_coligacoes_atualizadas = atualizar_qtd_votos_de_cada_coligacao(lista_de_candidatos, lista_de_coligacoes)
    quociente_eleitoral = obter_quociente_eleitoral(lista_de_candidatos, qtd_vagas_disponiveis)

    for coligacao in lista_de_coligacoes_atualizadas:
        vagas_obtidas = coligacao['total_votos'] // quociente_eleitoral
        coligacao['qtd_vagas'] += vagas_obtidas
        coligacao['votos_sobra_total'] = coligacao['total_votos'] % quociente_eleitoral
        qtd_vagas_disponiveis -= vagas_obtidas

    return lista_de_coligacoes_atualizadas, qtd_vagas_disponiveis


def distribuir_todas_as_vagas(lista_de_coligacoes: list, lista_de_candidatos: int, qtd_vagas_disponiveis: int):
    lista_atualizada, qtd_vagas_restante = atualizar_qtd_vagas_de_cada_coligacao(lista_de_coligacoes, lista_de_candidatos, qtd_vagas_disponiveis)

    while qtd_vagas_restante > 0:
        medias = lista_para_guardar_media(lista_de_coligacoes)
        index = 0

        for coligacao in lista_atualizada:
            media = coligacao['total_votos'] / (coligacao['qtd_vagas'] + 1)
            medias[index]['media'] = media
            index += 1

        maior_media =  reduzir(medias, lambda acumulado, x: obter_maior(acumulado, x['media']), 0)
        nome_da_coligacao_maior_media = obter_nome_da_coligacao_de_maior_media(medias, maior_media)
        incrementar_vaga(lista_atualizada, nome_da_coligacao_maior_media)
        qtd_vagas_restante -= 1

    return lista_atualizada


def obter_vereadores_eleitos(lista_de_coligacoes: list, lista_de_candidatos: int, qtd_vagas_disponiveis: int):
    lista_atualizada = distribuir_todas_as_vagas(lista_de_coligacoes, lista_de_candidatos, qtd_vagas_disponiveis)
    candidatos_eleitos = []

    for coligacao in lista_atualizada:

        candidatos_dessa_coligacao = filtrar(lista_de_candidatos, lambda candidato: candidato['coligacao'] == coligacao['coligacao'])
        lista_ordenada_dos_candidatos = sorted(candidatos_dessa_coligacao, key=lambda candidato: candidato['total_votos'], reverse=True)
        qtd_vagas = coligacao['qtd_vagas']
        eleitos_nessa_coligacao = lista_ordenada_dos_candidatos[:qtd_vagas]
        
        for eleito in eleitos_nessa_coligacao:
            candidatos_eleitos.append(eleito)

    return candidatos_eleitos
  

# FUNÇÕES DE EXIBIÇÃO


def exibir_total_de_votos_validos(lista_de_candidatos: list):
    qtd_votos_validos = obter_qtd_votos(lista_de_candidatos)
    print(f'Quantidade de votos válidos: {qtd_votos_validos}')


def exibir_quociente_eleitoral(lista_de_candidatos, qtd_vagas_disponiveis):
    quociente_eleitoral = obter_quociente_eleitoral(lista_de_candidatos, qtd_vagas_disponiveis)
    print(f'Quociente Eleitoral (QE): {quociente_eleitoral}')


def exibir_total_de_votos_por_coligacao(lista_de_candidatos: list, lista_de_coligacoes: list):
    lista_atualizada_com_votos = atualizar_qtd_votos_de_cada_coligacao(lista_de_candidatos, lista_de_coligacoes)
    lista_ordenada = sorted(lista_atualizada_com_votos, key=lambda coligacao: coligacao['total_votos'], reverse=True)

    print('-=-=-=-=-=-=-VOTOS POR COLIÇÃO-=-=-=-=-=-=-')

    for coligacao in lista_ordenada:
        print()
        espaco_necessario = obter_espaco_necessario(coligacao['coligacao'])
        print(f'{coligacao['coligacao']}:{espaco_necessario}{coligacao['total_votos']} votos válidos')
      

def exibir_vagas_por_quociente_partidario(lista_de_candidatos: list, qtd_vagas_disponiveis: int, lista_de_coligacoes: list):
    lista_atualizada, vagas_restantes = atualizar_qtd_vagas_de_cada_coligacao(lista_de_coligacoes, lista_de_candidatos, qtd_vagas_disponiveis)
    lista_ordenada = sorted(lista_atualizada, key=lambda coligacao: coligacao['qtd_vagas'], reverse=True)

    print('-=-=-VAGAS POR COLIGAÇÃO-=-=-=-')

    for coligacao in lista_ordenada:
        print()
        espaco_necessario = obter_espaco_necessario(coligacao['coligacao'])
        print(f'{coligacao['coligacao']}:{espaco_necessario}{coligacao['qtd_vagas']} vagas')
        print(coligacao['votos_sobra_total'])

    print(f' \n \nQuantidade de vagas que sobraram: {vagas_restantes} vagas\n ')   


def exibir_vagas_de_sobra(lista_de_coligacoes: list, lista_de_candidatos: list, qtd_vagas_disponiveis: int):
    lista_atualizada, qtd_vagas_restantes = atualizar_qtd_vagas_de_cada_coligacao(lista_de_coligacoes, lista_de_candidatos, qtd_vagas_disponiveis)
    copia_lista_atualizada = copy.deepcopy(lista_atualizada)
    lista_de_vagas_por_media = obter_lista_de_vagas_por_media(lista_atualizada)

    if qtd_vagas_restantes == 0:
        print('Não sobraram vagas, todas já foram distribuídas!')
        return
    
    print(f'Sobraram {qtd_vagas_restantes} vagas...\nVamos distribuí-las')
    enter_e_limpar()
    contador = 1

    while qtd_vagas_restantes > 0:
        medias = lista_para_guardar_media(lista_atualizada)
        index = 0

        print(f' \n \n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{contador}° MÉDIA-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n ')
        
        print('COLIGAÇÃO           |       CÁLCULO           |      MÉDIA')
        print('-----------------------------------------------------------------------')

        for coligacao in lista_atualizada:
            qtd_votos = coligacao['total_votos'] 
            qtd_vagas = coligacao['qtd_vagas']
            media = qtd_votos / (qtd_vagas + 1)
            medias[index]['media'] = media
            nome_coligacao = coligacao['coligacao']
            estrutura_calculo = f'{qtd_votos} / ({qtd_vagas} + 1)'
            espaco1 = obter_espaco_necessario(nome_coligacao)
            espaco2 = obter_espaco_necessario(estrutura_calculo)
            espaco3 = obter_espaco_necessario(str(media))
            print(f'{nome_coligacao}{espaco1}|     {estrutura_calculo}{espaco2}|      {media}{espaco3}') 
            index += 1
        
        maior_media = reduzir(medias, lambda acumulado, x: obter_maior(acumulado, x['media']), 0)
        nome_da_coligacao_maior_media = obter_nome_da_coligacao_de_maior_media(medias, maior_media)
        incrementar_vaga_da_media(lista_de_vagas_por_media, nome_da_coligacao_maior_media)
        incrementar_vaga(lista_atualizada, nome_da_coligacao_maior_media)
        qtd_vagas_restantes -= 1

        print(f' \n \nColigação que atingiu a maior média({contador}°) = Coligação {nome_da_coligacao_maior_media}')
        contador += 1

        enter_e_limpar() 

    resumo(lista_de_vagas_por_media, copia_lista_atualizada)

    return lista_atualizada


def exibir_vereadores_eleitos(lista_de_coligacoes: list, lista_de_candidatos: int, qtd_vagas_disponiveis: int):
    vereadores_eleitos = obter_vereadores_eleitos(lista_de_coligacoes, lista_de_candidatos, qtd_vagas_disponiveis)
    lista_ordenada = sorted(vereadores_eleitos, key=lambda vereador: vereador['total_votos'], reverse=True)
    contador = 1

    for eleito in lista_ordenada:
        print(descricao_eleitos(eleito, contador))
        contador += 1

        
def exibir_eleitos_sem_a_regra(lista_de_candidatos, qtd_vagas):
    lista_ordenada = sorted(lista_de_candidatos, key=lambda candidato: candidato['total_votos'], reverse=True)
    eleitos = lista_ordenada[:qtd_vagas]
    contador = 1

    for eleito in eleitos:
        print(descricao_eleitos(eleito, contador))
        contador += 1
    
    
    












            









    

    