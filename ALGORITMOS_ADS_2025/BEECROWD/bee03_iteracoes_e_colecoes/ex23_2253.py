def eh_caractere_proibido(caractere):
    return not eh_numero(caractere) and not eh_maiscula(caractere) and not eh_minuscula(caractere)


def tem_caractere_proibido(colecao):
    for item in colecao:
        if eh_caractere_proibido(item):
            return True
        
    return False    


def eh_numero(caractere):
    codigo = ord(caractere)
    return codigo >= 48 and codigo <= 57


def tem_numero(colecao):

    for item in colecao:
        if eh_numero(item):
            return True

    return False    
    

def eh_maiscula(letra):
    codigo = ord(letra)

    return codigo >= 65 and codigo <= 90


def eh_minuscula(letra):
    codigo = ord(letra)

    return codigo >= 97 and codigo <= 122


def tem_maiscula(colecao):
    for item in colecao:
        if eh_maiscula(item):
            return True

    return False


def tem_minuscula(colecao):
    for item in colecao:
        if eh_minuscula(item):
            return True

    return False    


def esta_no_intervalo(limite_min, limite_max, num):
    return num >= limite_min and num <= limite_max


def eh_valida(senha_criada):
    tamanho_senha = len(senha_criada)
    return esta_no_intervalo(6, 32, tamanho_senha) and tem_maiscula(senha_criada) and tem_minuscula(senha_criada) and tem_numero(senha_criada) and not tem_caractere_proibido(senha_criada)


def main():
    try:
        while True:
            senha_criada = input()
            if not senha_criada:
                break
            
            if eh_valida(senha_criada):
                print('Senha valida.')
            else:
                print('Senha invalida.')    
    
    except EOFError:
        pass        

main()



