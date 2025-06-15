def entradaFloat(label: str):
    entrada = input(label)
    try:
        entrada = float(entrada)
        return entrada
    except ValueError:
        print(f'O valor "{entrada}" não é um número real válido!')
        return entradaFloat(label)

def entradaInt(label: str):
    entrada = input(label)
    try:
        entrada = int(entrada)
        return entrada
    except ValueError:
        print(f'O valor "{entrada}" não é um número inteiro válido!')
        return entradaInt(label)


def validarNumLimiteFloat(num, limiteMin, limiteMax, label):
    if num >= limiteMin and num <= limiteMax:
        return num
    else:
        print(f'Entrada inválida, o valor precisa estar entre {limiteMin} e {limiteMax}')
        num = entradaFloat(label)
        return validarNumLimiteFloat(num, limiteMin, limiteMax, label)
    


def validarNumLimiteInt(num, limiteMin, limiteMax, label):
    if num >= limiteMin and num <= limiteMax:
        return num
    else:
        print(f'Entrada inválida, o valor precisa estar entre {limiteMin} e {limiteMax}')
        num = entradaInt(label)
        return validarNumLimiteFloat(num, limiteMin, limiteMax, label)
        

def validarLimiteMinFloat(num: float, limiteMin: float, label: str):
    if num >= limiteMin:
        return num
    else:
        print(f'Entrada inválida, O valor deve ser maior ou igual a {limiteMin}')    
        num = entradaFloat(label)
        return validarLimiteMinFloat(num, limiteMin, label)
    

def validarStr2Opcoes(resposta: str, opcao1: str, opcao2: str, label: str):
    if resposta == opcao1 or resposta == opcao2:
        return resposta
    else:
        print(f'Entrada inválida')    
        resposta = str(input(label))
        return validarStr2Opcoes(resposta, opcao1, opcao2, label)
    
    