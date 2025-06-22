def obterNumInteiro(label: str):
    try:
        num = int(input(label))
        return num
    except ValueError:
        print('Entrada invalida!\nO número inserido deve ser um inteiro válido')
        return obterNumInteiro(label)
    

def eh_divisor(candidato_divisor, num):
    return num % candidato_divisor == 0

    
def obterNumInteiroLimiteMin(label: str, limiteMin: int):
    num = obterNumInteiro(label)

    if num >= limiteMin:
        return num
    else:
        print(f'Entrada inválida\nO número inserido deve ser maior ou igual a {limiteMin}')
        return obterNumInteiroLimiteMin(label, limiteMin)
    

def obterNumReal(label: str):
    try:
        num = float(input(label))
        return num
    except ValueError:
        print('Entrada inválida!\nO número inserido deve ser um número real')
        return obterNumReal(label)


def obterNumRealLimiteMin(label: str, limiteMin: float):
    num = obterNumReal(label)

    if num >= limiteMin:
        return num
    else:
        print(f'Entrada inválida!\nO número inserido deve ser maior ou igual a {limiteMin}')
        return obterNumInteiroLimiteMin(label, limiteMin)
    
 
def obterNumRealPositivo(label: str):
    num = obterNumReal(label)

    if num >= 0:
        return num
    else:
        print('O número inserido deve ser um real positivo') 
        return obterNumRealPositivo(label)
    

def obterNumInteiroPositivo(label: str):
    num = obterNumInteiro(label)

    if num >= 0:
        return num
    else:
        print('O número inserido deve ser um inteiro positivo') 
        return obterNumInteiroPositivo(label)
         

def obter_inteiro_maior_que_0(label):

    while True:
        num = obterNumInteiro(label)

        if num > 0:
            return num

        print(f'Entrada inválida!\nO número inserido deve ser maior que 0')         


def obter_num_real_na_faixa(label, limite_min, limite_max):

    while True:
        num = obterNumReal(label)

        if num >= limite_min and num <= limite_max:
            return num
        
        print(f'Número inválido!\nO número inserido deve estar entre {limite_min} a {limite_max}')


    
    


