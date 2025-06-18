from time import sleep

def obter_num_inteiro(label):
    num = str(input(label))

    try:
        num = int(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número inteiro válido!')
        print(' ')
        return obter_num_inteiro(label)
    

def obter_inteiro_positivo(label: str):
    
    while True:
        num = obter_num_inteiro(label)

        if num >= 0:
            return num

        print('Entrada inválida!\nO número precisa ser um inteiro positivo') 


def obter_inteiro_maior_que_0(label: str):
    
    while True:
        num = obter_num_inteiro(label)

        if num > 0:
            return num

        print('Entrada inválida!\nO número precisa ser um inteiro maior que 0') 


def grande_espaco(qtd_linhas):
    for i in range(qtd_linhas):
        print( )



def obter_inteiro_no_intervalo(label: str, limite_min: int, limite_max: int):
    while True:
        num = obter_num_inteiro(label)

        if num >= limite_min and num <= limite_max:
            return num
        
        sleep(1)
        print(f'Entrada inválida!\nO número inserido deve estar entre {limite_min} e {limite_max}')
        sleep(1)
        print( )


def obter_num_real(label):
    num = str(input(label))

    try:
        num = float(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número real válido!')
        print(' ')
        return obter_num_real(label)


def obter_real_positivo(label: str):
    
    while True:
        num = obter_num_real(label)

        if num >= 0:
            return num

        print('Entrada inválida!\nO número precisa ser um real positivo') 

def obter_real_maior_que_0(label: str):
    
    while True:
        num = obter_num_real(label)

        if num > 0:
            return num

        print('Entrada inválida!\nO número precisa ser um real maior que 0') 



def obter_real_no_intervalo(label: str, limite_min: float, limite_max: float):
    while True:
        num = obter_num_real(label)

        if num >= limite_min and num <= limite_max:
            return num

        print(f'Entrada inválida!\nO número inserido deve estar entre {limite_min} e {limite_max}')


def avancar_posicoes(caractere, qtd_posicoes):
    codigo = ord(caractere)

    novo_codigo = codigo + qtd_posicoes
  
    return chr(novo_codigo)

def eh_letra_minuscula(caractere): 
    codigo = ord(caractere)

    return codigo >= 97 and codigo <= 122



def converter_maisculo(texto):
    novo_texto = ''
    
    for caractere in texto:
       
        if eh_letra_minuscula(caractere):
            caractere = avancar_posicoes(caractere, -32)
        
        novo_texto += caractere 
            
    return novo_texto          


