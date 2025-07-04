def obter_inteiro(label):
    while True:
        try:
            num = int(input(label))
            return num
        except ValueError:
            print('Entrada inválida!\nO valor inserido deve ser um número inteiro')


def obter_inteiro_na_faixa(label, limite_min, limite_max):
    while True:
        num = obter_inteiro(label)

        if num >= limite_min and num <= limite_max:
            return num
        
        print(f'Entrada inválida!\nO número inserido deve estar entre {limite_min} e {limite_max}')


def eh_letra_minuscula(caractere): 
    codigo = ord(caractere)

    return codigo >= 97 and codigo <= 122


def eh_letra_maiscula(caractere):
    codigo = ord(caractere)

    return codigo >= 65 and codigo <= 90


def eh_letra(caractere):
    codigo = ord(caractere)

    return (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)


def obter_uma_letra(label):
    while True:

        caractere = str(input(label))

        if len(caractere) == 1:
            if eh_letra(caractere):
                return caractere

        print('Entrada inválida!\nO caractere inserido deve ser uma letra e conter apenas 1 caractere')      


def avancar_posicoes(caractere, qtd_posicoes):
    codigo = ord(caractere)

    novo_codigo = codigo + qtd_posicoes
  
    return chr(novo_codigo)




def converter_maisculo(texto):
    novo_texto = ''
    
    for caractere in texto:
       
        if eh_letra_minuscula(caractere):
            caractere = avancar_posicoes(caractere, -32)
        
        novo_texto += caractere 
            
    return novo_texto


def esta_na_lista(caractere, lista):
    for i in lista:
        if caractere == i:
            return True
        
    return False



