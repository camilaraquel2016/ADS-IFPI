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
        return validarNumLimiteInt(num, limiteMin, limiteMax, label)
        

def validarLimiteMinFloat(num: float, limiteMin: float, label: str):
    if num >= limiteMin:
        return num
    else:
        print(f'Entrada inválida, O valor deve ser maior ou igual a {limiteMin}')    
        num = entradaFloat(label)
        return validarLimiteMinFloat(num, limiteMin, label)


def validarLimiteMinInt(num: int, limiteMin: int, label: str):
    if num >= limiteMin:
        return num
    else:
        print(f'Entrada inválida, O valor deve ser maior ou igual a {limiteMin}')    
        num = entradaInt(label)
        return validarLimiteMinInt(num, limiteMin, label)

def validarStr2Opcoes(resposta: str, opcao1: str, opcao2: str, label: str):
    if resposta == opcao1 or resposta == opcao2:
        return resposta
    else:
        print(f'Entrada inválida')    
        resposta = str(input(label))
        return validarStr2Opcoes(resposta, opcao1, opcao2, label)
    

def valorMilhar(num):
    return num // 1000


def valorCentena(num):
    return (num % 1000) // 100


def valorDezena(num):
    return (num % 100) // 10


def valorUnidade(num):
    return num % 10

def validarNum2Digitos(num: int, label: str):
    quociente = num // 10
    if quociente >= 1 and quociente <= 9:
        return num
    else:
        print('Entrada invalida! O número deve apresentar 2 dígitos')
        num = entradaInt(label)
        return validarNum2Digitos(num, label)
    

def maior3Num(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior


def menor3Num(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def eh_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 >= lado3 and lado1 + lado3 >= lado2 and lado2 + lado3 >= lado1



def pedirDia():
    dia = entradaInt('Insira o dia: ')

    if dia >= 1 and dia <= 31:
        return dia
    else:
        print('Dia inválido!\nO dia precisa estar entre 1 e 31')
        return pedirDia()


def pedirMes():
    mes = entradaInt('Insira o mês: ')

    if mes >= 1 and mes <= 12:
        return mes
    else:
        print('Mês inválido!\nO mês precisa estar entre 1 e 12')
        return pedirMes()


def pedirAno():
    ano = entradaInt('Insira o ano: ')

    if ano >= 1000 and ano <= 9999:
        return ano
    else:
        print('O ano precisa estar entre 1000 e 9999')
        return pedirAno()
    
def validarNum4Dig(num):
    if num >= 1000 and num <= 9999:
        return num
    else:
        print('O número deve possuir 4 dígitos')
        num = entradaInt('Digite o número de 4 dígitos: ')
        return validarNum4Dig(num)               