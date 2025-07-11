def esta_no_intervalo(limite_min, limite_max, num):
    return num >= limite_min and num <= limite_max


def obter_resposta(senha_criada):
    tamanho_senha = len(senha_criada)

    if esta_no_intervalo(6, 32, tamanho_senha) and tem_maiscula(senha_criada) and tem_minuscula(senha_criada) and 


def main():
    try:
        while True:
            senha_criada = input()
            if not senha_criada:
                continue
            resposta = obter_resposta(senha_criada)
    except EOFError:
        pass        
