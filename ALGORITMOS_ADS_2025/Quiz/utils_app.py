def carregar_perguntas_do_arquivo(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo)
    perguntas = []

    for linha in arquivo:
        dados = linha.strip().split('#')

        linha_pergunta = {

            'id': int(dados[0]),
            'pergunta': dados[1],
            'alternativas': [],
            'gabarito': dados[3].strip()
        }

        alternativas = dados[2].split('*')

        for alternativa in alternativas:
            letra = 


        

