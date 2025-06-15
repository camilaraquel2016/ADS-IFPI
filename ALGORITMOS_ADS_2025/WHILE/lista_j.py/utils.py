def obterNumReal(label): 
    while True:
        num = str(input(label))
        try:
            num = float(num)
            return num
        except ValueError:
            print(f'O valor "{num}" não é um número real válido!')
            

def obterNumInt(label):
    while True:
        num = str(input(label))
        try:
            num = int(num)
            return num
        except ValueError:
            print(f'O valor "{num}" não é um número inteiro válido!')



def limparTela():
    numDeLinhas = 40
    contador = 1

    while contador <= numDeLinhas:
        print(' ')
        contador += 1

def validarLimiteMin(min, num, label):
    while num < min:
        print(f'O número deve maior ou igual a {min}')
        num = obterNumInt(label)
    return num    

