def obterCentena(num):
    return num // 100


def obterDezena(num):
    return num % 100 // 10


def obterUnidade(num):
    return num % 10 // 1


def formatarCentena(num):
    centena = obterCentena(num)
    if centena == 0:
        return False
    elif centena == 1:
        return '1 centena'
    else:
        return f'{centena} centenas'
    


def formatarDezena(num):
    dezena = obterDezena(num)
    if dezena == 0:
        return False
    elif dezena == 1:
        return '1 dezena'
    else:
        return f'{dezena} dezenas'    
    


def formatarUnidade(num):
    unidade = obterUnidade(num)
    if unidade == 0:
        return False
    elif unidade == 1:
        return '1 unidade'
    else:
        return f'{unidade} unidades'


def formatarNum(num):
    centena = formatarCentena(num)
    dezena = formatarDezena(num)
    unidade = formatarUnidade(num)

    if formatarCentena(num):
        if formatarDezena(num):
            if formatarUnidade(num):
                return f'{centena}, {dezena} e {unidade}'
            else:
                return f'{centena} e {dezena}'
        else:
            if formatarUnidade(num):
                return f'{centena} e {unidade}'
            else:
                return f'{centena}'
    else:
        if formatarDezena(num):
            if formatarUnidade(num):
                return f'{dezena} e {unidade}'
            else:
                return f'{dezena}'
        else:
            return f'{unidade}'
        

def obterNum():
    num = abs(int(input('Insira o número: (1 a 999) ')))

    while num > 999:
        print('Número inválido')
        num = abs(int(input('Insira o número: (1 a 999) ')))
    return num    







def main():
    num = obterNum()
    print(formatarNum(num))
            

main()

