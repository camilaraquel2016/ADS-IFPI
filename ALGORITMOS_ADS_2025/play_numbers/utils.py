import os

def esta_na_lista(valor, lista):
    for item in lista:
        if valor == item:
            return True
        
    return False  


def obter_num_a_ser_removido(label: str, vetor: list, str_de_parada: str):
    while True:
        entrada = input(label).upper()

        if entrada == str_de_parada:
            return entrada
        
        try:
            num = float(entrada)  
            if esta_na_lista(num, vetor):
                return num
            print(f'O valor "{num}" não está presente no vetor, logo não pode ser removido.')

        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número real, no entanto você inseriu o valor "{entrada}"')


        input(' \nEnter para continuar...')
        limpar_tela()


def obter_valor_a_ser_adicionado(label: str, str_de_parada: str):
    while True:
        entrada = input(label).upper()

        if entrada == str_de_parada:
            return entrada
        
        try:
            num = float(entrada)  
            return num

        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número real, no entanto você inseriu o valor "{entrada}"')

        input(' \nEnter para continuar...')
        limpar_tela()


def limpar_tela():
    os.system('cls')


def obter_num_inteiro(label: str):
    while True:
        entrada = input(label)

        try:
            num = int(entrada)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número inteiro, entretanto você inseriu o valor "{entrada}"')


def obter_num_real(label: str):
    while True:
        entrada = input(label)

        try:
            num = float(entrada)
            return num
        except ValueError:
            print(f'Entrada inválida!\nO valor inserido deve ser um número real, entretanto você inseriu o valor "{entrada}"')            


def obter_num_inteiro_na_faixa(label: str, limite_min: int, limite_max: int):
    while True:
        num = obter_num_inteiro(label) 

        if num >= limite_min and num <= limite_max:
            return num
        
        print(f'Entrada inválida!\nO valor inserido deve estar entre {limite_min} e {limite_max}')

        input(' \nEnter para continuar...')
        limpar_tela()


def obter_opcao(label: str, limite_min: int, limite_max: int):

    while True:
        opcao = obter_num_inteiro(label)

        if opcao >= limite_min and opcao <= limite_max:
            return opcao
        
        print(f' \nOpcão inválida!\nA opção inserida deve esta entre {limite_min} e {limite_max}')

        input(' \nEnter para continuar...')
        limpar_tela()


def obter_num_inteiro_com_limite_min(label: str, limite_min: int):
    while True:
        num = obter_num_inteiro(label)

        if num >= limite_min:
            return num
        
        print(f'Entrada inválida!\nO valor inserido deve ser maior ou igual a {limite_min}')


def obter_num_real_com_limite_min(label: str, limite_min: float):
    while True:
        num = obter_num_real(label)

        if num >= limite_min:
            return num
        
        print(f'Entrada inválida!\nO valor inserido deve ser maior ou igual a {limite_min}')


def obter_num_real_na_faixa(label: str, limite_min: float, limite_max: float):
    while True:
        num = obter_num_real(label) 

        if num >= limite_min and num <= limite_max:
            return num
        
        print(f'Entrada inválida!\nO valor inserido deve estar entre {limite_min} e {limite_max}')

        input(' \nEnter para continuar...')
        limpar_tela()
