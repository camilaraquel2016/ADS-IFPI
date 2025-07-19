import os

def filtrar(colecao: list, funcao_criterio):
    nova_colecao = []

    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)

    return nova_colecao



def descricao_escola_geral(escola: dict, posicao: int):
    nome = escola['nome']
    cidade = escola['municipio']
    estado = escola['estado']
    rede = escola['rede']
    media_objetivas = escola['media_objetivas']
    redacao = escola['nota_redacao']
    media_total = (media_objetivas + redacao) / 2

    return f'''

    {posicao}. {nome} ({cidade} - {estado})
    Rede: {rede}
    Média das objetivas: {media_objetivas:.1f}
    Nota da Redação: {redacao:.1f}
    Média geral: {media_total:.1f}'''


def descricao_escola_por_area(escola: dict, posicao: int, area: str):
    nome = escola['nome']
    cidade = escola['municipio']
    estado = escola['estado']
    rede = escola['rede']
    media_objetivas = escola['media_objetivas']
    nota_na_area = escola[f'nota_{area}']

    return f'''

    {posicao}. {nome} ({cidade} - {estado})
    Rede: {rede}
    Média das objetivas: {media_objetivas:.1f}
    Nota de {formatar_area(area)}: {nota_na_area:.1f}'''


def esta_na_lista(item, lista: list):
    for item_da_vez in lista:
        if item_da_vez == item:
            return True
        
    return False     


def limpar_tela():
    os.system('cls')

def menu_regioes():
    return f'''
    -=-REGIÕES-=-
    1 - NORTE
    2 - NORDESTE
    3 - CENTRO-OESTE
    4 - SUDESTE
    5 - SUL

    >> '''


def obter_regiao(label: str):
    regioes = ['NORTE', 'NORDESTE', 'CENTRO-OESTE', 'SUDESTE', 'SUL']
    opcao = obter_num_inteiro_na_faixa(label, 1, len(regioes))
    return regioes[opcao - 1]


def obter_regioes_com_estados():
    regioes = {'NORTE': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
           'NORDESTE': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
           'CENTRO-OESTE': ['DF', 'GO', 'MT', 'MS'],
           'SUDESTE': ['ES', 'MG', 'RJ', 'SP'],
           'SUL': ['PR', 'RS', 'SC']}
    
    return regioes





def enter_e_limpar():
    input(' \nEnter para continuar...')
    limpar_tela()


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



def ordenar_por_todas_as_areas(lista_de_escolas: list):
    return sorted(lista_de_escolas, key=lambda escola: (escola['media_objetivas'] + escola['nota_redacao']) / 2, reverse=True)


def ordenar_por_area(lista_de_escolas: list, area: str):
    return sorted(lista_de_escolas, key=lambda escola: escola[f'nota_{area}'], reverse=True)


def formatar(texto: str):
    return texto.replace('‡Æo', 'ção')


def converter_para_real(nota: str):
    return float(nota.replace(',', '.'))


def obter_area(label: str):
    areas = ['linguagens', 'redacao', 'humanas', 'natureza', 'matematica']
    opcao = obter_num_inteiro_na_faixa(label, 1, len(areas))
    return areas[opcao - 1]

def formatar_area(area):
    areas = {'linguagens': 'Linguagens', 'redacao': 'Redação', 'humanas': 'Humanas', 'natureza': 'Natureza', 'matematica': 'Matemática'}
    return areas[area]   


def obter_estado(label: str):
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    opcao = obter_num_inteiro_na_faixa(label, 1, len(estados))
    return estados[opcao - 1]


def obter_rede(label: str):
    redes = ['Estadual', 'Federal', 'Municipal', 'Privada']
    opcao = obter_num_inteiro_na_faixa(label, 1, len(redes))
    return redes[opcao - 1]


def menu_areas():
    return f'''
    -=-=-ÁREAS DO CONHECIMENTO-=-=-
    1 - Linguagens
    2 - Redação
    3 - Humanas
    4 - Natureza
    5 - Matemática

    >> '''

def menu_redes():
    return f'''
    -=-=-REDE-=-=-
    1 - Estadual
    2 - Federal
    3 - Municipal
    4 - Privada

    >> '''

 
def menu_geral():
    return f'''
    -=-PROGRAMAS DE CONSULTAS (ENEM - 2014)-=-

       --------TOP N (1 Critério)-------

          1 - Top N Brasil (geral)
          2 - Top N Brasil por área
          3 - Top N por Região
          4 - Top N por Estado
          5 - Top N por Cidade
     
          
       --------Top N (2 Critérios)------

         6 - Top N por Região e Rede
         7 - Top N por Região e Área
         8 - Top N por Estado e Rede
         9 - Top N por Estado e Área
         10 - Melhor escola por Área e Estado


        -------OUTRAS CONSULTAS--------

         11 - Listar informações de uma escola
         12 - Listar todas as escolas de um Estado
         13 - Listar todas as escolas Privadas
         14 - Listar todas as escolas Públicas

         15 - Sair

        >> '''


def menu_estados():
    return f'''
    -=-ESTADOS-=-
     1 - AC
     2 - AL
     3 - AP
     4 - AM
     5 - BA
     6 - CE
     7 - DF
     8 - ES
     9 - GO
     10 - MA
     11 - MT
     12 - MS
     13 - MG
     14 - PA
     15 - PB
     16 - PR
     17 - PE
     18 - PI
     19 - RJ
     20 - RN
     21 - RS
     22 - RO
     23 - RR
     24 - SC
     25 - SP
     26 - SE
     27 - TO

    >> '''


def carregar_dados(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo)
    escolas = []

    for linha in arquivo:
        dados = linha.strip().split(';')

        escola = {
            'ranking': dados[0],
            'nome': dados[1],
            'municipio': dados[2],
            'estado': dados[3],
            'rede': dados[4], 
            'permanencia': dados[5],
            'nivel_socio_economico': formatar(dados[6]),
            'media_objetivas': converter_para_real(dados[7]),
            'nota_linguagens': converter_para_real(dados[8]),
            'nota_matematica': converter_para_real(dados[9]),
            'nota_natureza': converter_para_real(dados[10]),
            'nota_humanas': converter_para_real(dados[11]),
            'nota_redacao': converter_para_real(dados[12])
        }

        escolas.append(escola)

    return escolas    


def mapear(colecao: list, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    



def carregar_cidades(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo).readlines()
    return mapear(arquivo, lambda linha: linha.strip())
    


def obter_opcao_continuar(label: str):
    while True:
        opcao = input(label).upper()

        if opcao == 'S' or opcao == 'N':
            return opcao
        
        print('Opção inválida!\nInsira S ou N')


def reduzir(colecao, funcao_redutora, valor_inicial):
    acumulado = valor_inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado    

def obter_nome_escola(label):
    lista_de_escolas = carregar_dados(r'C:\Users\thali\OneDrive\Área de Trabalho\ads\ALGORITMOS_ADS_2025\programa_enem\enem2014_nota_por_escola.txt')

    while True:
        nome_escola = input(label).upper()
        
        for escola in lista_de_escolas:
            if nome_escola == escola['nome']:
                return nome_escola

        print(' \nEscola inválida!\n \nEssa escola não existe ou você escreveu o nome errado')
        enter_e_limpar()
